from .serializers import UserSerializer
from rest_framework import mixins, generics
from django.contrib.auth.models import User

class UserCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class UserListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class UserRetieveView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)