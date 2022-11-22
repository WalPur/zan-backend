# Generated by Django 4.1.3 on 2022-11-22 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PromoBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='promo_block', verbose_name='Баннер')),
                ('link', models.TextField(verbose_name='Ссылка (сайт, видео)')),
                ('show_on_main', models.BooleanField(verbose_name='Отображать на главной')),
            ],
        ),
    ]
