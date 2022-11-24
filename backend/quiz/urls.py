from rest_framework.routers import DefaultRouter

from .views import (
    QuizAdminDetailEndpoint,
)


router = DefaultRouter()

router.register(
    'quizadmindetail', 
    QuizAdminDetailEndpoint, 
    basename="quiz-admin-derail"
)

urlpatterns = [] + router.urls
