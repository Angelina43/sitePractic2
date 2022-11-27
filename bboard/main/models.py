from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import Signal
from django.utils.crypto import get_random_string

user_registrated = Signal('instance')


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    middle_name = models.CharField(max_length=50, blank=True, null=True, default='', verbose_name='Отчество')
    apply_personal_data = models.BooleanField(default=False,
                                              verbose_name='Согласие на обработку персональных данных')

    class Meta(AbstractUser.Meta):
        pass
