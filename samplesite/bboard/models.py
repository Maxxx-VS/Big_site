from django.db import models

class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(verbose_name="Описаие")
    price = models.FloatField(verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявление"
        ordering = ['-published']