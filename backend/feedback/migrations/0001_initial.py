# Generated by Django 4.1.3 on 2022-11-23 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('USER', 'Пользователь'), ('STAFF', 'Работник')], max_length=120, verbose_name='Пользователь или гражаданин')),
                ('email', models.TextField(blank=True, verbose_name='Электронная почта')),
                ('phone_number', models.TextField(verbose_name='Номер телефона')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('full_name', models.TextField(blank=True, verbose_name='ФИО')),
                ('user_id', models.IntegerField(blank=True, verbose_name='ID пользователя')),
                ('first_name', models.TextField(blank=True, verbose_name='Фамилия')),
                ('middle_name', models.TextField(blank=True, verbose_name='Имя')),
                ('last_name', models.TextField(blank=True, verbose_name='Отчество')),
            ],
        ),
    ]
