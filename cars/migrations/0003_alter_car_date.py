# Generated by Django 3.2.3 on 2021-05-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_image_min_car_image_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateField(),
        ),
    ]
