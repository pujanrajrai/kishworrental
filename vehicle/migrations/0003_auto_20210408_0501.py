# Generated by Django 3.1.7 on 2021-04-08 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20210408_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='number_plate',
            field=models.CharField(default='aaa', max_length=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle',
            field=models.ImageField(default='a.txt', upload_to=''),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='is_available',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
