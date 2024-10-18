from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from My_Music_App.profiles.validators import username_validation


class Profile(models.Model):

    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[MinLengthValidator(2), username_validation],
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0.0)]
    )

    class Meta:
        db_table = 'Profiles'
