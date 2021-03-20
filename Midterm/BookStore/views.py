from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from BookStore.models import Book, Journal
from .serializer import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = BookSerializer(user)
        return Response(serializer.data)


class JournalViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        queryset = Journal.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = JournalSerializer(user)
        return Response(serializer.data)


