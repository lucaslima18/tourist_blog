from django.urls import path, include
from rest_framework import routers
from blog.api import viewsets

from blog.views import PostsList


router = routers.DefaultRouter()
router.register('posts', viewsets.PostViewSet)

urlpatterns = [
    path('', PostsList.as_view(), name="post_list"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='api'))
]
