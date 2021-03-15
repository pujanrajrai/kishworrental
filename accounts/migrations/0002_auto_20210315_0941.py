# Generated by Django 3.1.7 on 2021-03-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='Username'),
            preserve_default=False,
        ),
    ]
