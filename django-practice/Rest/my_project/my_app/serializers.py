from rest_framework import serializers
from .models import Book, Cohort

class BookSerializer(serializers.ModelSerializer):
    #days_since = 
    class Meta:
        model = Book
        fields = '__all__'


class CohortSerializer(serializers.ModelSerializer):
     class Meta:
         model = Cohort
         fields  = "__all__"