from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model


from .validators import validate_price

User = get_user_model()


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
    author = models.ForeignKey(
        User, verbose_name='Автор Записи', on_delete=models.CASCADE, null=True
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('title', 'description'), name='unique_title_contest'),
        )

class Congratulation(models.Model):
    text = models.TextField('Комментарий')
    comment_area = models.ForeignKey(
        Contest,
        on_delete=models.CASCADE,
        related_name='Комментарий'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)



