from django.core.validators import MinLengthValidator
from django.db import models

from myPlantApp.web.validators import name_validator, only_letters_validator


class Profile(models.Model):
    MAX_USERNAME_LEN = 10
    MIN_USERNAME_LEN = 2
    MAX_FIRST_NAME_LEN = 20
    MAX_LAST_NAME_LEN = 20

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_USERNAME_LEN,
        validators=(
            MinLengthValidator(MIN_USERNAME_LEN),
        ),
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            name_validator,
        ),
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            name_validator,
        ),
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    MAX_TYPE_LEN = 14
    MAX_NAME_LEN = 20
    MIN_NAME_LEN = 2

    PLANTS = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_TYPE_LEN,
        choices=PLANTS,
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_NAME_LEN),
            only_letters_validator,
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
