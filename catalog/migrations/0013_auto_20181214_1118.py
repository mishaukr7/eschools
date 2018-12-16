# Generated by Django 2.1.4 on 2018-12-14 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_product_product_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Відгук', 'verbose_name_plural': 'Відгуки'},
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.Product'),
        ),
    ]
