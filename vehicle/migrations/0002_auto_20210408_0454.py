# Generated by Django 3.1.7 on 2021-04-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='seat',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
