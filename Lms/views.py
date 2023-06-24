from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from Lms.filter import AuthorFilter, BookFilter
from Lms.models import Author, Book
from Lms.pagination import DefaultPagination
from Lms.serializers import AuthorSerializer, BookSerializer
from rest_framework import status


# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']
    permission_classes = [DjangoModelPermissions]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_set_class = BookFilter
    search_fields = ['title']
    permission_classes = [IsAdminUser]


#
class AuthorList(ListCreateAPIView):
    def get_queryset(self):
        return Author.objects.all()


#     def get_serializer_class(self):
#         return AuthorSerializer
#
#
class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializers = AuthorSerializer(authors, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialize = AuthorSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response("SUCCESS", status=status.HTTP_201_CREATED)


def send_mail_function(request):
    send_mail("library message", "your book order is now available", "timothy2@gmail.com",
              ["ojokwan@gmail.com"])
    return HttpResponse("its sent")

#
# class AuthorDatailView(APIView):
#     def get(self, request, pk):
#         author = Author.objects.get(pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = Author.objects.get(pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Successfully updated", status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         author = Author.objects.get(pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view()
# def all_author(request):
#     authors = Author.objects.all()
#     return render(request, 'home.html', {"authors": authors})
#
#
# @api_view(['GET', 'POST'])
# def all_books(request):
#     if request.method == 'GET':
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True, context={'request': request})
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response('Added Successful', status=status.HTTP_200_OK)
#
#
# @api_view(['Get', 'PUT'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         # book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # serializer.validated_data()
#         serializer.save()
#         return Response("ADDED Successful", status=status.HTTP_200_OK)

#
# @api_view(['GET', 'POST'])
# def list_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializers = AuthorSerializer(authors, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serialize = AuthorSerializer(data=request.data)
#         serialize.is_valid(raise_exception=True)
#         # serialize.validated_data()
#         serialize.save()
#         return Response("SUCCESS", status=status.HTTP_201_CREATED)
#

# @api_view()
# def welcome(request):
#     return Response('this is a demo')

# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         # author = Author.objects.get(pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Successfully updated", status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         # if author.book_set.count() > 0:
#         #     return Response({"ERROR": "Author associated with a book and cannot be deleted"},
#         #                     status=status.HTTP_204_NO_CONTENT)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1MTE0NDI1LCJpYXQiOjE2ODUxMTQxMjUsImp0aSI6ImYxZGUxYTY0NDA1NTQ5MDc5MWJhYWU2YTdlNWViZmFkIiwidXNlcl9pZCI6MX0.20ulHMCGBgCLQ-ATmnaddM7J6qYoJmJPPUG8uiAO27Y"
