from django.db import models

class PromoBlock(models.Model):
    banner = models.ImageField(upload_to="promo_block", verbose_name="Баннер")
    link = models.TextField(verbose_name="Ссылка (сайт, видео)")
    show_on_main = models.BooleanField(verbose_name="Отображать на главной")
