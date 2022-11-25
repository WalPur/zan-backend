from django.db import models

class Partner(models.Model):
    name = models.TextField(verbose_name="Название")
    preview = models.ImageField(
        verbose_name="Превью компании",
        upload_to='partners/previews',
    )
    banner = models.ImageField(
        verbose_name="Баннер компании",
        upload_to="partners/banners",
    )
    description = models.TextField(verbose_name="Описание")
    is_active = models.BooleanField(verbose_name="Компания активна", default=1)
    show_on_main = models.BooleanField(
        verbose_name="Отображать на главной",
        default=1
    )
