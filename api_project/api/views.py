from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
	authentication_classes = [TokenAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

	queryset = Book.objects.all()
	serializer_class = BookSerializer