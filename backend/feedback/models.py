from django.db import models


class UserType(models.TextChoices):
    USER = 'USER', 'Пользователь'
    STAFF = 'STAFF', 'Работник'


class Feedback(models.Model):
    # common fields
    user_type = models.CharField(
        verbose_name="Пользователь или гражданин", 
        max_length=120, 
        choices=UserType.choices
    )
    email = models.TextField(verbose_name="Электронная почта", blank=True)
    phone_number = models.TextField(verbose_name="Номер телефона")
    message = models.TextField(verbose_name="Сообщение")
    is_readed = models.BooleanField(verbose_name="Прочитано", default=False)
    
    # citizen fields
    full_name = models.TextField(verbose_name="ФИО", blank=True)

    # staff fields
    user_id = models.IntegerField(
        verbose_name="ID пользователя", 
        blank=True,
        default=0
    )
    first_name = models.TextField(verbose_name="Фамилия", blank=True)
    middle_name = models.TextField(verbose_name="Имя", blank=True)
    last_name = models.TextField(verbose_name="Отчество", blank=True)


class StaffPins(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    file = models.FileField(
        verbose_name="Прикрепление", upload_to='feedback_pins', null=True
    )
