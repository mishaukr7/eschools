# Generated by Django 2.1.4 on 2018-12-10 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181210_1319'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productcharacteristic',
            unique_together={('product', 'characteristic_type', 'name', 'value')},
        ),
    ]