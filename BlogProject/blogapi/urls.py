from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import PostingView, ReplesView

router = DefaultRouter()
router.register(r"posts", PostingView, basename="post")

replesRouter = routers.NestedDefaultRouter(router, r'posts', lookup='post')
replesRouter.register(r"reples", ReplesView, basename="reple")


urlpatterns = [
    path('', include(router.urls)),
    path('', include(replesRouter.urls))
]