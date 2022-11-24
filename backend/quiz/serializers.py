from rest_framework import serializers

from .models import (
    Quiz,
    QuizQuestion,
    QuizAnswerVariant,
    QuizResult,
    QuizAnswerChoosen
)

class QuizQuestionVariants(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswerVariant
        fields = (
            'answer_variant',
            'is_right'
        )


class QuizQuestions(serializers.ModelSerializer):
    variants = QuizQuestionVariants(many=True)

    class Meta:
        model = QuizQuestion
        fields = (
            'question',
            'question_type',
            'reward',
            'variants'
        )


class QuizAdminDetail(serializers.ModelSerializer):
    questions = QuizQuestions(many=True)

    class Meta:
        model = Quiz
        fields = (
            'id',
            'name',
            'plank',
            'success_text',
            'failure_text',
            'questions'
        )
