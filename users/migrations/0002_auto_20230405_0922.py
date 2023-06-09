# Generated by Django 3.0 on 2023-04-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile',
            field=models.ImageField(upload_to='images/profile/'),
        ),
    ]
