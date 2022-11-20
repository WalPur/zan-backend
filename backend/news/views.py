from rest_framework import viewsets

from .models import (
    Article
)

from .serializator import (
    NewsSerializer,
    NewsListSerializer,
)

class NewsEndpoint(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    http_method_names = ['get', 'post']
    serializer_class = NewsSerializer


class NewsListEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return Article.objects.all().order_by('-pub_date')