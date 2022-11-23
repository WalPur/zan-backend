from rest_framework import viewsets

from .models import (
    Feedback,
    StaffPins
)

from .serializators import (
    FeedbackWeb,
    FeedbackAdminList,
    FeedbackAdminDetail
)

class FeedbackWebEndpoint(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = FeedbackWeb

class FeedbackAdminListEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = FeedbackAdminList
    def get_queryset(self):
        objects = Feedback.objects.all()
        for object in objects:
            if object.user_type == "STAFF":
                object.full_name = object.first_name + " " + object.middle_name + " " + object.last_name
        return objects


class FeedbackAdminDetalEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = FeedbackAdminDetail
    queryset = Feedback.objects.all()
