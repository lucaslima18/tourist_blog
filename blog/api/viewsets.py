from blog.api.serializers import PostSerializer
from blog.models import Post
from rest_framework import permissions, viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permissions_class = [permissions.IsAuthenticated]
