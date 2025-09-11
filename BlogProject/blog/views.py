from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import PostSerializer

from .models import Posting, Reples

from drf_spectacular.utils import extend_schema


#게시글 목록 조회, 생성, 조회, 수정, 삭제 구현
class PostListCreateAPIView(APIView):
    @extend_schema(operation_id="post_list")
    def get(self, request):
        posting = Posting.objects.all()
        serializer = PostSerializer(posting, many=True)

        return Response(serializer.data)
    
    @extend_schema(
            request=PostSerializer,
            responses={201: PostSerializer},
            operation_id="post_create"
    )
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    @extend_schema(operation_id="post_retrieve")
    def get(self, request, pk):
        post = get_object_or_404(Posting, pk=pk)

        serializer = PostSerializer(post)
        return Response(post.data)
    
    @extend_schema(
            request=PostSerializer,
            responses={200: PostSerializer},
            operation_id="post_update"
    )
    def put(self, request, pk):
        post = get_object_or_404(Posting, pk=pk)
        serializer = PostSerializer(post, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(operation_id="post_destroy")
    def delete(self, request, pk):
        post = get_object_or_404(Posting, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
