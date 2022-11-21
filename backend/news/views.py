from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated 
)
from rest_framework import viewsets, filters

from .models import (
    Article
)

from .serializator import (
    NewsSerializer,
    NewsListSerializer,
)

class NewsEndpoint(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    http_method_names = ['get', 'post', 'patch']
    permission_classes = [IsAuthenticatedOrReadOnly ]
    serializer_class = NewsSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'name', 'text', 'pub_date')
    ordering = ('id')


class NewsListEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    serializer_class = NewsListSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'name', 'text', 'pub_date')
    ordering = ('id')

    def get_queryset(self):
        return Article.objects.all().order_by('-pub_date')