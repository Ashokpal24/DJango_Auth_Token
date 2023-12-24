from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserRegisterationView(APIView):
    def get(self, request, format=None):
        return Response({'msg': "Registeration Success"}, status=status.HTTP_201_CREATED)
