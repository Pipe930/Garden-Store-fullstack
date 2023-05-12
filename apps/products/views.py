from rest_framework.response import Response
from rest_framework import generics, status, filters
from django.http import Http404
from .models import Category, Product, Offer
from .serializer import CategorySerializer, ProductSerializer, OfferSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# View that lists all categories
class ListCategoriesView(generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('name_category')
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        queryset = self.get_queryset() # Get the queryset

        if len(queryset):
            serializer = self.get_serializer(queryset, many=True) # The data is serialized
            return Response({"categories": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not Data Found'}, status=status.HTTP_204_NO_CONTENT)

# View to create a new category
class CreateCategoryView(generics.CreateAPIView):

    serializer_class = CategorySerializer
    parser_classes = [JSONParser]
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # Petition POST
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data) # The data is serialized

        if serializer.is_valid(): # The data is validated
            serializer.save() # The data is save
            return Response(
                {
                    "data": serializer.data,
                    "message": "Created category successfully"
                 }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to obtain a category
class CategoryDetailView(generics.RetrieveAPIView):

    serializer_class = CategorySerializer
    parser_classes = [JSONParser]

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

        return Response(serializer.data, status=status.HTTP_200_OK)

# View to update a category
class UpdateCategoryView(generics.UpdateAPIView):

    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    parser_classes = [JSONParser]
    serializer_class = CategorySerializer

    def get_object(self, id:int):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

        return category

    def put(self, request, id:int, format=None):

        category = self.get_object(id)
        serializer = self.get_serializer(category, data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(                {
                    "data": serializer.data,
                    "message": "Updated category successfully"
                 }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to delete a category
class DeleteCategoryView(generics.DestroyAPIView):

    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id:int):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

        return category

    def delete(self, request, id:int, format=None):

        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
