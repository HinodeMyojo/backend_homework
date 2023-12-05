from datetime import date

from django.core.exceptions import ValidationError

def validate_price(value: int) -> None:
    if value < 1 or value > 100:
        raise ValidationError(
            'Цена должна быть в диапазоне от 1 до 100'
        )