# Generated by Django 5.1.4 on 2025-01-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_house', '0003_appartments_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartments',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
