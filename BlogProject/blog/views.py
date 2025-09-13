from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from rest_framework.exceptions import ValidationError

from .serializers import PostSerializer, RepleSerializer

from .models import Posting, Reples

# PostListCreateAPIView, PostDetailView

class PostListCreateAPIView(
    GenericAPIView, ListModelMixin, CreateModelMixin
):
    queryset = Posting.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
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

#아직 미구현!
class ReplesCreateView(
    GenericAPIView, CreateModelMixin
):
    queryset = Reples.objects.all()
    serializer_class = RepleSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        try:
            post_pk = self.kwargs.get("post_id")
            post = Posting.objects.get(pk=post_pk)
            serializer.save(post=post)
        
        except Posting.DoesNotExist:
            raise ValidationError({"detail": "해당 게시글을 찾을 수 없습니다."})
    

class ReplesDetailView(
    GenericAPIView, UpdateModelMixin, DestroyModelMixin
):
    queryset = Reples.objects.all()
    serializer_class = RepleSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)