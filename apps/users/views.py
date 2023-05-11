from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .models import User
from .serializers import UserSerializer

# View that lists registered users
class UserListView(generics.ListAPIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    #Petition GET
    def get(self, request):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if len(serializer.data):
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'Usuarios Not Found'}, status=status.HTTP_204_NO_CONTENT)

# View that a user registered
class DetailUserView(generics.RetrieveAPIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self, id:int):

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

        return user

    def get(self, request, id:int, format=None):
        user = self.get_object(id)
        serializer = self.get_serializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
