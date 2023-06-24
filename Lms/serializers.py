from decimal import Decimal

from djoser.serializers import UserCreateSerializer as BasedUserCreateSerializer
from djoser.serializers import UserSerializer as BasedCurrentUserSerializer
from rest_framework import serializers

from Lms.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'email']
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    # date_of_birth = serializers.DateField()


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'language', 'genre', 'book_number', 'discount_price']

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author-detail')
    book_number = serializers.CharField(max_length=15, source='isbn')
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    # title = serializers.CharField(max_length=250)
    # author = serializers.CharField(max_length=50)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def calculate(self, book: Book):
        return book.price * Decimal(0.1)


class UserCreateSerializer(BasedUserCreateSerializer):
    class Meta(BasedUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class CurrentUserSerializer(BasedCurrentUserSerializer):
    class Meta(BasedCurrentUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
