from rest_framework import generics

from blogs.models import Blog

from .serializer import BlogSerializer

from rest_framework.renderers import (
    BrowsableAPIRenderer,
    JSONRenderer,
)
from rest_framework.permissions import AllowAny


class BlogCreateListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    renderer_classes = [
        # BrowsableAPIRenderer,
        JSONRenderer,
    ]
    permission_classes = [AllowAny]
