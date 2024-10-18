
from django.core.exceptions import ValidationError


def username_validation(username):
    for char in username:
        if not char.isalnum() and char != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")