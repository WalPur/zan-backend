from rest_framework import serializers
from rest_framework.serializers import FileField

from .models import Feedback, StaffPins

class FileSerializer(serializers.ModelSerializer):
    file = FileField(read_only=True)

    class Meta:
        model = StaffPins
        fields = ('id', 'file')


class FeedbackWeb(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'full_name',
            'email',
            'phone_number',
            'message'
        )

class FeedbackAdminList(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'full_name',
            'user_type',
            'is_readed',
            'message',
        )

class FeedbackAdminDetail(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()


    class Meta:
        model = Feedback
        fields = (
            'id',
            'full_name',
            'first_name',
            'middle_name',
            'last_name',
            'user_type',
            'is_readed',
            'message',
            'files'
        )
    
    @staticmethod
    def get_files(obj):
        return FileSerializer(
            StaffPins.objects.filter(feedback=obj.id),
            many=True
        ).data
