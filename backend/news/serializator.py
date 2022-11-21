from rest_framework import serializers
from rest_framework.serializers import ImageField

from .models import (
    Article,
    ArticleImage,
)


class ImageSerializer(serializers.ModelSerializer):
    image = ImageField(read_only=True)

    class Meta:
        model = ArticleImage
        fields = ('id', 'image')


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(
            max_length = 1000000, allow_empty_file = False, use_url = False
        ),
        write_only = True
    )

    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "text",
            "pub_date",
            "uploaded_images",
            "video",
            "image"
        )

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_article = Article.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            new_article_image = ArticleImage.objects.create(
                article = new_article, image = uploaded_item
            )
        return new_article

    @staticmethod
    def get_image(obj):
        return ImageSerializer(
            ArticleImage.objects.filter(article=obj.id),
            many=True
        ).data


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "id",
            "name",
            "text",
            "pub_date",
        )
