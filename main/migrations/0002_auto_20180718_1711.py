# Generated by Django 2.0.7 on 2018-07-18 15:11

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usercode',
            field=models.CharField(default=main.models.create_profile_usercode, max_length=100),
        ),
    ]
