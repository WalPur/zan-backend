from django.db import models

from partners.models import Partner

class ScheduleTypes(models.TextChoices):
    # График работы блять
    FULL = 'FULL', 'Полный рабочий день'
    TURN = 'TURN', 'Сменный график'
    FLOAT = 'FLOAT', 'Гибкий график'
    WATCH = 'WATCH', 'Вахтовый метод'
    IRREGULAR = 'IRREGULAR', 'Ненормированный рабочий день'
    PART_TIME = 'PART_TIME', 'Неполный рабочий день'


class BusyTypes(models.TextChoices):
    # Тип занятости сука
    FULL = 'FULL', 'Полная занятость'
    PARTIAL = 'PARTIAL', 'Частичная занятость'
    PROJECT = 'PROJECT', 'Временная'
    PROBATION = 'PROBATION', 'Стажировка'
    SEOSONAL = 'SEOSONAL', 'Сезонная'
    REMOTE = 'REMOTE', 'Удаленная'


class EducationType(models.TextChoices):
    MIDDLE = 'MIDDLE', 'Среднее'
    MIDDLE_SPECIAL = 'MIDDLE_SPECIAL', 'Среднее профессиональное'
    UNFINISHED_HIGH = 'UNFINISHED_HIGH', 'Неоконченное высшее'
    HIGH = 'HIGH', 'Высшее'



class Vacation(models.Model):
    company = models.ForeignKey(
        Partner, on_delete=models.CASCADE, verbose_name="Партнер"
    )
    is_active = models.BooleanField(verbose_name="Вакансия активна", default=1)
    desc = models.TextField(verbose_name="Описание вакансии")
    logo = models.ImageField(
        verbose_name="Логотип",
        upload_to="vacations/logos"
    )
    site = models.TextField(verbose_name="Сайт компании")
    inn = models.TextField(verbose_name="ИНН")
    adress = models.TextField(verbose_name="Адрес")
    city_or_discrict = models.TextField(verbose_name="Город или район")
    move_support = models.BooleanField(
        verbose_name="Поддержка при переезде", 
        default=0,
        blank=True
    )
    population_support = models.BooleanField(
        verbose_name="Поддержка при населении", 
        default=0,
        blank=True
    )
    living = models.BooleanField(
        verbose_name="Предоставление жилья", 
        default=0,
        blank=True
    )
    # profession
    # sphere
    min_salary = models.IntegerField(
        verbose_name="Минимальная зарплата",
        blank=True,
        default=0
    )
    max_salary = models.IntegerField(
        verbose_name="Максимальная зарплата",
        blank=True,
        default=0
    )
    scheduleType = models.CharField(
        verbose_name="Тип занятости", 
        max_length=120, 
        choices=ScheduleTypes.choices
    )
    busyType = models.CharField(
        verbose_name="Тип занятости", 
        max_length=120, 
        choices=BusyTypes.choices
    )

