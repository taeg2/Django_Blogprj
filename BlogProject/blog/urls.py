from django.urls import path

from .views import PostListCreateAPIView, PostDetailView

urlpatterns = [
    path("", PostListCreateAPIView.as_view(), name="post_list_view"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail_view")
]