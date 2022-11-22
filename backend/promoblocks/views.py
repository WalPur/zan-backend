from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated 
)
from rest_framework import viewsets, filters

from .models import (
    PromoBlock
)

from .serializators import (
    PromoAdminDetailSerializer,
    PromoAdminListSerializer,
)

class PromoAdminListEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch']
    # permission_classes = [IsAuthenticated]
    serializer_class = PromoAdminListSerializer

    def get_queryset(self):
        return PromoBlock.objects.all().order_by('id')


class PromoAdminDetailEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch', 'delete', 'post']
    # permission_classes = [IsAuthenticated]
    serializer_class = PromoAdminDetailSerializer

    def get_queryset(self):
        return PromoBlock.objects.all().order_by('id')

class PromoMainEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = PromoAdminDetailSerializer

    def get_queryset(self):
        return PromoBlock.objects.all().order_by('id')