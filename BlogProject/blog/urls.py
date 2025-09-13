from django.urls import path

from .views import PostListCreateAPIView, PostDetailView, ReplesCreateView, ReplesDetailView

urlpatterns = [
    path("post/", PostListCreateAPIView.as_view(), name="post_list_view"),
    path("post/<int:post_id>/", PostDetailView.as_view(), name="post_detail_view"),
    path("post/<int:post_id>/reples/", ReplesCreateView.as_view(), name="reples_create_view"),
    path("reples/<int:pk>/", ReplesDetailView.as_view(), name="reples_detail_view")
]