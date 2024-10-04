from django.shortcuts import render
from rest_framework import generics
from .models import Book, Cohort
from .serializers import BookSerializer, CohortSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()

    serializer_class = BookSerializer

#When you want to control whats going on
"""class CohortViewSet2(viewsets.ViewSet):
    def list (self, request):
        queryset = Cohort.objects.all()
        serializer = CohortSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        cohort = Cohort.objects.filter(pk=pk).first()
        if not cohort:
            message = {"detail":f"This id {pk} cohort doesn't exist"}
            return Response(message, status=404)
        serializer = CohortSerializer(cohort)
        return Response(serializer.data)
    
    def create(self, request, pk=None):
        queryset =Cohort.objects.create(**request.data)
        serializer = CohortSerializer(queryset)
        return Response(serializer.data)
   
    def update(self, request, pk=None):
        queryset =Cohort.objects.update(**request.data)
        serializer = CohortSerializer
        return Response(serializer.data)



    def partial_update(self, request, pk=None):
        pass
 
 
    def destroy(self, request, pk=None):
        queryset = Cohort.objects.delete(pk=pk)
        serializer = CohortSerializer(queryset)
        return Response(serializer.data)
     """


#This is used when you don't want to have control of all django methods
class CohortViewSet(viewsets.ModelViewSet):
    serializer_class = CohortSerializer
    queryset = Cohort.objects.all()
