from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import UserRegisterationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from Auth.renderers import UserRenderer


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
