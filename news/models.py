from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    date_pub = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    date_mod = models.DateField(auto_now=True, verbose_name='Дата модификации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



