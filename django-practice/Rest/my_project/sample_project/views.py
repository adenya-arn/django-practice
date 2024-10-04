from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Comment, CommentSerializer

# Create your views here.


@api_view(["GET"])
def hello(request):
    comment = Comment(email="aadenya7@gmail.com", content="I am trying django")

    serializer = CommentSerializer(comment)
    print(serializer.data)

    serializer2 = CommentSerializer(data=serializer.data)
    if serializer2.is_valid():
        print(f"{serializer2.validated_data}")
    return Response({"data": serializer.data})
