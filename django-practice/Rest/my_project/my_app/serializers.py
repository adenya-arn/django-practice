from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    #days_since = 
    class Meta:
        model = Book
        fields = '__all__'