# Generated by Django 2.1.4 on 2018-12-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=400)),
                ('content', models.TextField(max_length=4096)),
                ('video', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
