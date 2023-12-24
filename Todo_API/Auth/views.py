from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import (
    UserRegisterationSerializer,
    UserLoginSerializer,
    UserProfileSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from Auth.renderers import UserRenderer
from django.contrib.auth import authenticate


def get_tokens_from_user(user):
    refresh = RefreshToken.for_user(user)
    print(refresh)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class UserRegisterationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegisterationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_from_user(user)
        return Response({'token': token, 'msg': 'Registration Sucessful'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token = get_tokens_from_user(user)
            return Response({'token': token, 'msg': 'Login Success'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'errors':
                             {'non_field_errors': [
                                 'Email or Password is not Valid']}},
                            status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
