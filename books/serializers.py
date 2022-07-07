from rest_framework import serializers
from .models import Customer, Book, Burgain

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BurgainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burgain
        fields = "__all__"