# Generated by Django 3.1.7 on 2021-03-14 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_post',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
