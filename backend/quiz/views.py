from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import (
    Quiz,
    QuizQuestion,
    QuizAnswerVariant,
)

from .serializers import (
    QuizAdminDetail,
)

class QuizAdminDetailEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = QuizAdminDetail
    queryset = Quiz.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            questions = serializer.validated_data.pop('questions')
            quiz = Quiz.objects.create(**serializer.validated_data)
            for question in questions:
                question['quiz'] = quiz
                variants = question.pop('variants')
                o_question = QuizQuestion.objects.create(**question)
                for variant in variants:
                    variant['question'] = o_question
                    QuizAnswerVariant.objects.create(**variant)
            return Response(
                serializer.validated_data, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)