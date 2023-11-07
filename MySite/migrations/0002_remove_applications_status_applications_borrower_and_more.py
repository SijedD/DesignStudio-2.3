# Generated by Django 4.2.7 on 2023-11-07 02:24

import MySite.models
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='Status',
        ),
        migrations.AddField(
            model_name='applications',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applications',
            name='design_image',
            field=models.ImageField(default=None, help_text='Разрешается формата файла только jpg, jpeg, png, bmp', upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']), MySite.models.Applications.validate_image], verbose_name='Дизайн'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MySite.category'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='date_create',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='time_create',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Введите категорию', max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='applications',
            name='status',
            field=models.CharField(blank=True, choices=[('Новая', 'Новая'), ('Принято в работу', 'Принято в работу'), ('Выполнено', 'Выполнено')], default='Новая', max_length=16, verbose_name='Статус'),
        ),
    ]
