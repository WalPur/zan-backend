from django.db import models


class FormType(models.TextChoices):
    QUIZ = 'QUIZ', 'Опрос'
    TEST = 'TEST', 'Тестирование'


class Quiz(models.Model):
    type = models.CharField(
        verbose_name="Тип формы",
        max_length=120,
        choices=FormType.choices
    )
    name = models.TextField(verbose_name="Название тестирования/опроса")
    plank = models.IntegerField(
        verbose_name="Количество баллов для прохождения тестов",
        blank=True,
        default=0
    )
    success_text = models.TextField(verbose_name="Успешный итоговый текст")
    failure_text = models.TextField(verbose_name="Провальный итоговый текст")


class QuestionType(models.TextChoices):
    RADIO = 'RADIO', 'Один из множества'
    CHECKBOX = 'CHECKBOX', 'Несколько вариантов'
    OPEN = 'OPEN', 'Открытый'


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name="Связанный опрос/тестирование"
    )
    question = models.TextField(verbose_name="Вопрос")
    question_type = models.CharField(
        verbose_name="Тип вопроса",
        max_length=120,
        choices=QuestionType.choices
    )
    reward = models.IntegerField(
        verbose_name="Баллы за правильный ответ",
        blank=True,
        default=0
    )


class QuizAnswerVariant(models.Model):
    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        verbose_name="Связанный опрос/тестирование"
    )
    answer_variant = models.TextField("Вариант ответа")
    is_right = models.BooleanField(
        verbose_name="Правильный или нет",
        default=0
    )


class QuizResult(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name="Связанный опрос/тестирование"
    )
    total = models.IntegerField(
        verbose_name="В общем баллов",
        default=0,
        blank=True,
    )
    passed = models.BooleanField(
        verbose_name="Пройдено или нет",
        default=0,
        blank=True,
    )

class QuizAnswerChoosen(models.Model):
    result = models.ForeignKey(
        QuizResult,
        on_delete=models.CASCADE,
        verbose_name="Связанный общий результат"
    )
    question = models.ForeignKey(
        QuizQuestion,
        on_delete=models.CASCADE,
        verbose_name="Связанный вопрос"
    )
    is_right = models.BooleanField(
        verbose_name="Выбрано правильно или нет",
        default=0,
        blank=True,
    )
    text = models.TextField(
        verbose_name="Ответ на открытый вопрос",
        default="",
        blank=True
    )
