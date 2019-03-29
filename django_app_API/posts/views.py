from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from .models import Post


class PostsList(viewsets.ModelViewSet):
    """  """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permissions for Post objects
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        """ Assigning current authenticated user as post author """
        serializer.save(author=self.request.user)
