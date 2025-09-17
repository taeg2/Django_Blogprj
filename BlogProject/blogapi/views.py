from rest_framework import viewsets
from rest_framework import mixins

from blog.models import Posting, Reples

from .serializers import PostingSerializer, ReplesSerailzer

class PostingView(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class ReplesView(mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    queryset = Reples.objects.all()
    serializer_class = ReplesSerailzer

    def get_queryset(self):
        return Reples.objects.filter(posting_id = self.kwargs['post_id'])