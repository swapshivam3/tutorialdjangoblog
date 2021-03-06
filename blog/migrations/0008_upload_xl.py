# Generated by Django 3.1.7 on 2021-05-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_XL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='xl')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
    ]
