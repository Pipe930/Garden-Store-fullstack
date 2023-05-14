from rest_framework import status, generics
from rest_framework.response import Response
from .models import Cart, CartItems
from django.http import Http404
from .serializer import CartSerializer, AddCartItemSerializer, SubtractCartItemSerializer, ClearCartSerializer, VoucherSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser

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

        cart = self.get_object(idUser)

        serializer = self.get_serializer(cart)

        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateCartView(generics.CreateAPIView):

    serializer_class = CartSerializer
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddCartItemView(generics.CreateAPIView):

    serializer_class = AddCartItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubtractCartItemView(generics.CreateAPIView):

    serializer_class = SubtractCartItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({"message": "Se resto el producto"}, status=status.HTTP_200_OK)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClearCartItemsView(generics.DestroyAPIView):

    serializer_class = ClearCartSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id:int):

        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            raise Http404

        return cart

    def delete(self, request, id:int, format=None):

        cart = self.get_object(id)

        items = CartItems.objects.filter(id_cart = cart.id)

        if len(items):

            for item in items:
                item.delete()

            return Response({"message": "El carrito se a limpiado con exito"}, status=status.HTTP_204_NO_CONTENT)

        return Response({"message": "Tu carrito esta vacio"}, status=status.HTTP_204_NO_CONTENT)


class CreateVoucherView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    parser_classes = [JSONParser]
    serializer_class = VoucherSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "message": "Se creo la compra con exito"
                    }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
