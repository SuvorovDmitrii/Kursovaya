# Generated by Django 4.1.7 on 2023-03-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_alter_request_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]
