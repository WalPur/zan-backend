from rest_framework.routers import DefaultRouter

from .views import (
    PromoAdminListEndpoint,
    PromoAdminDetailEndpoint,
    PromoMainEndpoint
)


router = DefaultRouter()

# router.register('news', NewsEndpoint, basename='news')
router.register('promolist', PromoAdminListEndpoint, basename='promo-list')
router.register(
    'promodetail', PromoAdminDetailEndpoint, basename='promo-detail'
)
router.register(
    'promo', PromoMainEndpoint, basename='promo'
)

urlpatterns = [] + router.urls