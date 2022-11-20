from django.db import models


class Article(models.Model):
    name = models.TextField(verbose_name="Название")
    video = models.FileField(
        upload_to='videos_uploaded', null=True,
    )
    text = models.TextField(verbose_name="Текст")
    url = models.TextField(verbose_name="Ссылка (источник)", blank=True)
    pub_date = models.DateField(auto_now=True)


class ArticleImage(models.Model):
    article = models.ForeignKey(
        "Article", verbose_name="Новость", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="news_image", verbose_name="Картинка"
    )