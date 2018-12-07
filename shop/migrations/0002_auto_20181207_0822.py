# Generated by Django 2.1.4 on 2018-12-07 08:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created', '-updated']},
        ),
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата створення'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shop/news/'),
        ),
        migrations.AddField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата оновлення'),
        ),
    ]