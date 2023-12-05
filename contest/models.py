from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_price


class Contest(models.Model):
    title = models.CharField(verbose_name='Название', max_length=20)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена',
        validators=[MinValueValidator(10), MaxValueValidator(100), validate_price],
        help_text='Рекомендованная розничная цена',
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True)
    image = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        upload_to='contest_images')

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('title', 'description'), name='unique_title_contest'),
        )

    