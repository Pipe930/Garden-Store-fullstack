from rest_framework import status, generics
from rest_framework.response import Response
from .models import Order, Region, Province, Commune, Branch
from .serializer import OrderSerializer, RegionSerializer, ProvinceSerializer, CommuneSerializer, BranchSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser

class ListOrdersView(generics.ListAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if len(serializer.data):

            return Response({"orders": serializer.data}, status.HTTP_200_OK)

        return Response({"message": "No hay pedidos registrados"}, status.HTTP_204_NO_CONTENT)

class DetailOrderView(generics.RetrieveAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id:int):

        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise Http404

        return order

    def get(self, request, id:int, format=None):

        order = self.get_object(id)
        serializer = self.get_serializer(order)

        return Response(serializer.data, status.HTTP_200_OK)

class CreateOrderView(generics.CreateAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    parser_classes = [JSONParser]

    def post(self, request, format=None):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "data": serializer.data,
                    "message": "pedido creado con exito"
                    }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ListRegionsView(generics.ListAPIView):

    permission_classes = [AllowAny]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get(self, request, format=None):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if len(serializer.data):

            return Response({"regions": serializer.data}, status.HTTP_200_OK)

        return Response({"message": "No tenemos regiones registradas"}, status.HTTP_204_NO_CONTENT)

class ListProvincesView(generics.ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = ProvinceSerializer

    def get(self, request, id:int):

        queryset = Province.objects.filter(id_region = id)
        serializer = self.get_serializer(queryset, many=True)

        return Response({"provinces": serializer.data}, status.HTTP_200_OK)

class ListCommunesView(generics.ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = CommuneSerializer

    def get(self, request, id:int):

        queryset = Commune.objects.filter(id_province = id)
        serializer = self.get_serializer(queryset, many=True)

        return Response({"communes": serializer.data}, status.HTTP_200_OK)

class ListBranchView(generics.ListAPIView):

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if len(serializer.data):

            return Response({"branches": serializer.data}, status.HTTP_200_OK)

        return Response({"message": "No tenemos sucursales registradas"}, status.HTTP_204_NO_CONTENT)
