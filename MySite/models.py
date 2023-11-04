from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    name = models.CharField(max_length=250, verbose_name="ФИО", help_text="Только кириллические буквы, дефис и пробелы")
    username = models.CharField(max_length=35, verbose_name="Логин", unique=True,
                                help_text="Только латиница и дефис, уникальный")
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Согласен с обработкой '
                                                    'персональных данных?')


class Meta(AbstractUser.Meta):
    pass


class Category(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите категорию")

    def __str__(self):
        return self.name


class Applications(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    title = models.CharField(max_length=100)
    deck = models.TextField(max_length=1000, default='something')
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    date_create = models.DateField(default=datetime.now, verbose_name="Дата создания")
    time_create = models.TimeField(default=datetime.now, verbose_name="Время создания")
    image = models.ImageField(upload_to="media/", verbose_name="Фотография",
                              help_text="Разрешается формата файла только jpg, jpeg, png, bmp",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']),
                                          validate_image])
    REQUEST_STATUS = (
        ('Новая', 'Новая'),
        ('Принято в работу', 'Принято в работу'),
        ('Выполнено', 'Выполнено'),
    )
    status = models.CharField(
        max_length=16,
        choices=REQUEST_STATUS,
        default='Новая',
        blank=True,
        verbose_name="Статус")
    borrower = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
