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


class Order(models.Model):
    name = models.CharField(max_length=254, verbose_name='Название', blank=False)
    about = models.TextField(verbose_name='Описание', blank=False)
    date = models.DateField(verbose_name='Дата добавления', blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE, default='1')
    image = models.ImageField(max_length=254, upload_to=get_name_file,
                              blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='Наимнование', blank=False)

    def __str__(self):
        return self.name
