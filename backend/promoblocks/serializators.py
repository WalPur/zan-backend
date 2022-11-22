from rest_framework import serializers

from .models import PromoBlock

class PromoAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoBlock
        fields = (
            'id',
            'banner',
            'show_on_main',
        )


class PromoAdminDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoBlock
        fields = (
            'banner',
            'show_on_main',
            'link'
        )
