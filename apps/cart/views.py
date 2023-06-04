from rest_framework import status, generics
from rest_framework.response import Response
from .models import Cart, CartItems, Voucher
from rest_framework.authtoken.models import Token
from apps.products.models import Product
from django.http import Http404, HttpResponse
from .serializer import CartSerializer, AddCartItemSerializer, SubtractCartItemSerializer, VoucherSerializer, CancelVoucherSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from .cart_total import calculate_total_quality, calculate_total_products, cart_total
from rest_framework.authentication import get_authorization_header

def token_validated(request, idUser:int):

    token = get_authorization_header(request).split()
    token = token[1].decode()

    tokenDB = Token.objects.get(key = token)

    if tokenDB.user.id == idUser:
        return True

    return False

class CartUserView(generics.RetrieveAPIView):

    serializer_class = CartSerializer
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, idUser:int):

        try:
            cart = Cart.objects.get(id_user=idUser)
        except Cart.DoesNotExist:
            raise Http404

        return cart

    def get(self, request, idUser:int, format=None):

        if not token_validated(request, idUser):
            return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

        cart = self.get_object(idUser)

        serializer = self.get_serializer(cart)

        return Response(serializer.data, status.HTTP_200_OK)

class CreateCartView(generics.CreateAPIView):

    serializer_class = CartSerializer
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class AddCartItemView(generics.CreateAPIView):

    serializer_class = AddCartItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id:int):

        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

        return product

    def create(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            data = serializer.data

            if not token_validated(request, data["id_user"]):
                return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

            product = self.get_object(data["product"])

            quantity = data["quantity"]

            if product.stock < quantity:

                return Response({"message": "La cantidad supera el stock disponible"}, status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({"data": serializer.data, "message": "Agregado al carrito con exito"}, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class DeleteProductCartView(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id_cart:int, id_product:int):

        try:
            product = CartItems.objects.get(id_cart=id_cart, product=id_product)
        except CartItems.DoesNotExist:
            raise Http404

        try:
            cart = Cart.objects.get(id=id_cart)
        except Cart.DoesNotExist:
            raise Http404

        return product, cart

    def delete(self, request, id_cart:int, id_product:int):

        product, cart = self.get_object(id_cart, id_product)

        if not token_validated(request, cart.id_user.id):
            return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

        product.delete()

        return Response({"message": "Producto Eliminado"}, status.HTTP_200_OK)

class SubtractCartItemView(generics.CreateAPIView):

    serializer_class = SubtractCartItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            data = serializer.data

            if not token_validated(request, data["id_user"]):
                return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

            serializer.save()

            return Response({"message": "Se resto el producto"}, status.HTTP_200_OK)


        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ClearCartItemsView(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id:int):

        try:
            cart = Cart.objects.get(id_user=id)
        except Cart.DoesNotExist:
            raise Http404

        return cart

    def delete(self, request, id:int, format=None):

        if not token_validated(request, id):
            return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

        cart = self.get_object(id)

        items = CartItems.objects.filter(id_cart = cart.id)

        if len(items):

            for item in items:
                item.delete()

            cart_total(cart)
            calculate_total_products(cart.id)
            calculate_total_quality(cart.id)

            return Response({"message": "El carrito se a limpiado con exito"}, status.HTTP_204_NO_CONTENT)

        return Response({"message": "Tu carrito esta vacio"}, status.HTTP_204_NO_CONTENT)


class CreateVoucherView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    parser_classes = [JSONParser]
    serializer_class = VoucherSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not token_validated(request, request.data["id_user"]):
                return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

            products = request.data["products"]

            if products == {}:
                return Response({"message": "El json no puede estar vacio"}, status.HTTP_400_BAD_REQUEST)

            try:
                products["items"]
            except KeyError:
                return Response({"message": "El json no es valido"}, status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "message": "Se creo la compra con exito"
                    }, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class CancelPurchaseView(generics.UpdateAPIView):

    serializer_class = CancelVoucherSerializer
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id:int):

        try:
            voucher = Voucher.objects.get(id=id)
        except Voucher.DoesNotExist:
            raise Http404

        return voucher

    def put(self, request, id:int):

        voucher = self.get_object(id)
        serializer = self.get_serializer(voucher, data=request.data)

        if serializer.is_valid():

            if not token_validated(request, request.data["id_user"]):
                return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

            data = serializer.validated_data

            if data["state"]:
                data["state"] = False

            if not voucher.state:
                return Response({"message": "Esta compra esta cancelada"}, status.HTTP_406_NOT_ACCEPTABLE)

            products = voucher.products
            items = products["items"]

            for item in items:

                id = item["id"]
                quantity = item["quantity"]
                product = Product.objects.get(id=id)

                new_stock = product.stock + quantity

                product.stock = new_stock
                product.save()

            serializer.save()
            return Response({"message": "Se a cancelado la compra"}, status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ListVouchersView(generics.ListAPIView):

    serializer_class = VoucherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id:int, format=None):

        if not token_validated(request, id):
            return Response({"message": "Este token no le pertenece a este usuario"}, status.HTTP_401_UNAUTHORIZED)

        queryset = Voucher.objects.filter(id_user=id, state=True).order_by("created")
        serializer = self.get_serializer(queryset, many=True)

        if len(serializer.data):

            return Response(serializer.data, status.HTTP_200_OK)

        return Response({"message":"No haz realizado ninguna compra"}, status.HTTP_204_NO_CONTENT)

class DetailVoucherView(generics.RetrieveAPIView):

    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id:int):

        try:
            voucher = Voucher.objects.get(id=id)
        except Voucher.DoesNotExist:
            raise Http404

        return voucher

    def get(self, request, id:int):

        voucher = self.get_object(id)
        serializer = self.get_serializer(voucher)

        return Response(serializer.data, status.HTTP_200_OK)

