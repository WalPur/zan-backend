# Generated by Django 4.1.3 on 2022-11-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_feedback_user_id_alter_feedback_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_id',
            field=models.IntegerField(blank=True, default='USER', verbose_name='ID пользователя'),
        ),
    ]
