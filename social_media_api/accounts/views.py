from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status

class RegisterAPIView(generics.CreateAPIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	model = CustomUser.objects.all()
	serializer_class = UserSerializer

class LoginView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username, password=password)
		if user:
			token, _ = Token.objects.get_or_create(user=user)
			return Response({"token": token.key})
		return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		return Response({"message": "Welcome to the profile page!"})