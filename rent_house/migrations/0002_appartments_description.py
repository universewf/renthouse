# Generated by Django 5.1.4 on 2025-01-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartments',
            name='description',
            field=models.CharField(default=1, max_length=255, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
