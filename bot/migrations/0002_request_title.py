# Generated by Django 4.2 on 2023-05-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Заголовок'),
        ),
    ]
