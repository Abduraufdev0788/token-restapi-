from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from .serializers import RegisterSerializers, UserSerializers, LoginSerializers


class Register(APIView):
    def post(self, request:Request)->Response:
        serializer = RegisterSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            user_json = UserSerializers(user).data

            return Response(user_json, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class Login(APIView):
    def post(self, request:Request)->Response:
        serializer = LoginSerializers(data=request.data)

        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user = authenticate(username = data['username'], password = data['password'])

            if user is not None:

                token, created = Token.objects.get_or_create(user=user)

                return Response({"token": token.key}, status=status.HTTP_201_CREATED)
            
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request:Request)->Response:
        request.user.auth_token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

        

