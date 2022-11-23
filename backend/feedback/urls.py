from rest_framework.routers import DefaultRouter

from .views import (
    FeedbackWebEndpoint,
    FeedbackAdminListEndpoint,
    FeedbackAdminDetalEndpoint,
)

router = DefaultRouter()

router.register('feedbackuser', FeedbackWebEndpoint, basename='user-feedback')
router.register(
    'feedbackadminlist', 
    FeedbackAdminListEndpoint, 
    basename='admin-feedback-list'
)
router.register(
    'feedbackadmindetail',
    FeedbackAdminDetalEndpoint,
    basename='admin-feedback-detail'
)

urlpatterns = [] + router.urls
