# Generated by Django 4.2 on 2023-04-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Номер телефона')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]