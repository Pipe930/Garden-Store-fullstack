from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login, logout
from .models import User, Subscription
from .serializers import UserSerializer, SubscriptionSerializer, MessageSerializer, ChangePasswordSerializer
from django.contrib.sessions.models import Session
from datetime import datetime
from .util import Util
from apps.cart.models import Cart
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from rest_framework.parsers import JSONParser

# View that the user registers in the system
class RegisterUserView(generics.CreateAPIView):

    serializer_class = UserSerializer
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]

    def post(self, request):

        # Serializer data
        serializer = self.get_serializer(data=request.data)

                # Is the data valid?
        if serializer.is_valid():

            serializer.save() # Save the data

            return Response({
                "data": serializer.data,
                "message": "Se Registro Correctamente"
                }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View that authenticates the user
class LoginView(ObtainAuthToken):

    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):

        # The request is serialized
        serializer = self.serializer_class(
            data=request.data
        )

        if serializer.is_valid():

            user_found = authenticate(
                username = request.data["username"],
                password = request.data["password"]
            )

            if user_found is not None: # user found?

                serializer.is_valid(raise_exception=True)
                user = serializer.validated_data["user"] # User is obtained

                if user.is_active: # Is the user active?

                    token, created = Token.objects.get_or_create(user=user) # A token is created for the user
                    cart, createCart = Cart.objects.get_or_create(id_user=user) # A cart is created for the user

                    if created: # If a token exists

                        login(request=request, user=user) # The user is authenticated

                        userJson = {
                            "token": token.key,
                            "username": user.username,
                            "user_id": user.id,
                            "activate": user.is_active,
                            "staff": user.is_staff,
                            "idCart": cart.id
                        }

                        return Response(userJson, status=status.HTTP_200_OK) # Response

                    # If there is not token
                    token.delete() # Remove Token
                    token = Token.objects.create(user=user) # A new token is created

                    # User information
                    userJson = {
                        "token": token.key,
                        "username": user.username,
                        "user_id": user.id,
                        "activate": user.is_active,
                        "staff": user.is_staff,
                        "idCart": cart.id
                    }

                    return Response(userJson, status=status.HTTP_200_OK) # Response

                return Response({"message": "El usuario no esta activo"}, status= status.HTTP_401_UNAUTHORIZED)

            return Response({"message": "Credenciales Invalidas"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to logout the user
class LogoutView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            # The token is obtained in the parameters of the url
            tokenUrl = request.GET.get("token") # The token is obtained from the url parameter "token"
            token = Token.objects.filter(key=tokenUrl).first()

            if token: # Is there a token?
                user = token.user # Obtain user
                all_sesion = Session.objects.filter(expire_date__gte = datetime.now()) # You get all sessions

                if all_sesion.exists(): # Is there an active session?

                    for session in all_sesion:
                        session_data = session.get_decoded() # Decode the session

                        if user.id == int(session_data.get("_auth_user_id")): # Is there an active session with this user?
                            session.delete() # delete session

                token.delete()
                logout(request=request)

                # Messages
                session_message = "Session de usuario terminada"
                token_message = "Token Eliminado"

                # Message in json format
                message = {
                    "sesion_message": session_message,
                    "token_message": token_message
                }

                return Response(message, status=status.HTTP_200_OK)

            return Response({"error": "Usuario no encontrado con esas credenciales"},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"errors": "El token no se a encontrado en la cabecera"}, status=status.HTTP_409_CONFLICT)

# View that creates and lists subscriptions
class ListSubscriptionView(generics.ListAPIView):

    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    queryset = Subscription.objects.all()

    # Petition GET
    def get(self, request):

        queryset = self.get_queryset() # get queryset
        serializer = self.get_serializer(queryset, many=True) # The data is serialized

        return Response({"subscriptions": serializer.data}, status=status.HTTP_200_OK)

class CreateSubscriptionView(generics.CreateAPIView):

    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = SubscriptionSerializer

    # Petition POST
    def post(self, request, format=None):

        serializer = self.get_serializer(data=request.data) # The data is serialized

        if serializer.is_valid(): # Validation of received data

            serializer.save() # The data is save
            return Response(
                {
                    "data": serializer.data,
                    "message": "Subscripcion Creada con Exito"
                },
                status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View that gets a subscription by id
class SubscriptionDetailView(generics.RetrieveDestroyAPIView):

    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # Get the object by id
    def get_object(self, id:int):
        try:
            subscription = Subscription.objects.get(id=id) # Queryset
        except Subscription.DoesNotExist:
            # If it does not exist, it returns a 404 message
            raise Http404

        return subscription

    # Petition GET
    def get(self, request, id:int, format=None):

        subcription = self.get_object(id) # Object
        serializer = self.get_serializer(subcription) # Serializer data

        return Response(serializer.data, status=status.HTTP_200_OK)

    # Petition DELETE
    def delete(self, request, id:int, format=None):

        subscription = self.get_object(id) # Object
        subscription.delete() # Delete a Object subscription

        return Response(status=status.HTTP_204_NO_CONTENT)

# View for mailing
class SendEmailView(generics.CreateAPIView):

    serializer_class = MessageSerializer
    parser_classes = [JSONParser]

    # Petition POST
    def post(self, request, format=None):

        serializer = self.get_serializer(data=request.data) # The data is serialized

        if serializer.is_valid(): # The information is validated

            print(serializer.data)
            Util.send_email(data=serializer.data) # The method of the util send email class is used

            return Response({"data": serializer.data, "message": "Email enviado con exito"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View that changes the user"s password
class ChangePasswordView(generics.UpdateAPIView):
    """
    One end point to change the password
    """
    serializer_class = ChangePasswordSerializer
    model = User
    parser_classes = [JSONParser]

    # Get the user object
    def get_object(self, queryset=None):

        object = self.request.user
        return object

    # Petition PUT
    def update(self, request, *args, **kwargs):

        self.object = self.get_object() # Is obtained a user
        serializer = self.get_serializer(data=request.data) # The data is serialized

        if serializer.is_valid(): # The date is validated

            # Check if the password is correct
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # The password that the user will get is encrypted
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save() # The new password is saved

            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Contraseña actualizada con exito",
                "data": []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # Email Message
    email_plaintext_message = "{}?token={}".format(reverse("password_reset:reset-password-request"), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Garden Store"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
