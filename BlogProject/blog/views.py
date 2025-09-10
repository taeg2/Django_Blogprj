from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)

#게시글 목록 조회, 생성, 조회, 수정, 삭제 구현
class PostListandCreate(
    GenericAPIView, ListModelMixin, CreateModelMixin
):
    "아직 미구현"