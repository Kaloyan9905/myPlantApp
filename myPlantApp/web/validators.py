import re
import string

from django.core.exceptions import ValidationError


def name_validator(value):
    if not value[0] == value[0].upper():
        raise ValidationError('Your name must start with a capital letter!')


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')
