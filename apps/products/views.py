from rest_framework.response import Response
from rest_framework import generics, status, filters
from django.http import Http404
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

# View that lists all categories
class ListCategoriesView(generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("name_category")
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        queryset = self.get_queryset() # Get the queryset

        if len(queryset):
            serializer = self.get_serializer(queryset, many=True) # The data is serialized
            return Response(serializer.data, status.HTTP_200_OK)

        return Response({"message": "No tenemos categorias registradas"}, status.HTTP_204_NO_CONTENT)

# View to obtain a category
class CategoryDetailView(generics.RetrieveAPIView):

    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    # Fuction to obtain a object category
    def get_object(self, id:int):
        try:
            category = Category.objects.get(id=id) # Get object category
        except Category.DoesNotExist:
            raise Http404

        return category

    # Petition GET
    def get(self, request, id:int, format=None):

        category = self.get_object(id) # Category
        serializer = self.get_serializer(category) # The data is serialized

        return Response(serializer.data, status.HTTP_200_OK)

# View that list all products
class ListProductsPageView(generics.ListAPIView):


    queryset = Product.objects.filter(condition=True, id_offer__isnull= True).order_by("name_product")
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        queryset = self.get_queryset() # get queryset
        page = self.paginate_queryset(queryset) # paginate queryset
        serializer = self.get_serializer(page, many=True) # The data is serialized

        if len(serializer.data): # Is the list empty?
            return self.get_paginated_response(serializer.data)

        return Response({"message": "No tenemos productos registrados"}, status.HTTP_204_NO_CONTENT)

class ListProductsView(generics.ListAPIView):

    queryset = Product.objects.filter(condition=True, id_offer__isnull= True).order_by("name_product")
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        queryset = self.get_queryset() # get queryset
        serializer = self.get_serializer(queryset, many=True) # The data is serialized

        if len(serializer.data): # Is the list empty?
            return Response(serializer.data, status.HTTP_200_OK)

        return Response({"message": "No tenemos productos registrados"}, status.HTTP_204_NO_CONTENT)

# View for obtain is a product
class ProductView(generics.RetrieveAPIView):

    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_object(self, slug:str):
        try:
            product = Product.objects.get(slug=slug) # Get object product
        except Product.DoesNotExist: # If it doesn"t exist
            raise Http404

        return product

    def get(self, request, slug:str, format=None):
        product = self.get_object(slug) # get object
        serializer = self.get_serializer(product) # The data is serialized

        return Response(serializer.data, status.HTTP_200_OK)

# View for search a product
class ProductSearchView(generics.ListAPIView):

    queryset = Product.objects.filter(condition=True, id_offer__isnull= True).order_by("name_product")
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter] # Filter Backend Search Product
    search_fields = ["name_product"] # Field to search for a product
    permission_classes = [AllowAny]

class ListProductOfferView(generics.ListAPIView):

    queryset = Product.objects.filter(condition=True, id_offer__isnull=False).order_by("name_product")
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        product = self.get_queryset() # Get queryset
        page = self.paginate_queryset(product) # Paginate queryset
        serializer = self.get_serializer(page, many=True) # The data is serialized

        if len(serializer.data): # Is the list empty?

            return self.get_paginated_response(serializer.data)

        return Response({"detail": "No se encontradon productos en oferta"}, status.HTTP_204_NO_CONTENT)

class ProductFilterView(generics.ListAPIView):

    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get(self, request, id:int):

        # Query filter by category id
        query = Product.objects.filter(
            condition = True, id_offer__isnull = True, id_category = id
            ).order_by("name_product")

        serializer = self.get_serializer(query, many=True) # The data is serialized

        return Response(serializer.data, status.HTTP_200_OK)
