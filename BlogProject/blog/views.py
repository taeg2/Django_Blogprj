from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)

from .serializers import PostSerializer

from .models import Posting

# PostListCreateAPIView, PostDetailView

class PostListCreateAPIView(
    GenericAPIView, ListModelMixin, CreateModelMixin
):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.post(request)
    
class PostDetailView(
    GenericAPIView, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin
):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args):
        return self.retrieve(request, *args)
    
    def put(self, request, *args):
        return self.update(request, *args)
    
    def delete(self, request, *args):
        return self.destroy(request, *args)
