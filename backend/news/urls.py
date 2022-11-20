from rest_framework.routers import DefaultRouter

from .views import (
    NewsEndpoint,
    NewsListEndpoint
)


router = DefaultRouter()

router.register('news', NewsEndpoint, basename='news')
router.register('news/<int:pk>', NewsEndpoint, basename='news')
router.register('newslist', NewsListEndpoint, basename='news-list')

urlpatterns = [] + router.urls