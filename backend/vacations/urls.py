from django.urls import path

from .views import (
    Trudvsem
)


urlpatterns = [
    path('trudvsem', Trudvsem.as_view()),
]
