# Generated by Django 2.1.4 on 2018-12-06 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181206_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.DecimalField(blank=True, decimal_places=0, error_messages={'min_value': 'Номер телефону вказується без вісімки, повинен містити 10 цифр і не повинен починатися з нуля', 'unique': 'Пользователь с таким номера телефона уже существует'}, max_digits=10, null=True, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)], verbose_name='номер телефона'),
        ),
    ]
