from django.db import models
from tinymce import models as tinymce_models

class Service(models.Model):
    title=models.CharField(verbose_name="Наименование услуги",max_length=255,default="")
    image=models.ImageField(verbose_name="Изображение услуги")
    description=models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name='Услуга'
        verbose_name_plural='Услуги'

    def __str__(self) -> str:
        return self.title



class Portfolio(models.Model):
    title=models.CharField(verbose_name='Название проекта',max_length=255)
    info=models.TextField(verbose_name='Информация о проекте',null=True,blank=True)
    image=models.ImageField(verbose_name='Изображение проекта')

    class Meta:
        verbose_name='Портфолио'
        verbose_name_plural='Портфолио'

    def __str__(self) -> str:
        return self.title

class OurClients(models.Model):
    title=models.CharField(verbose_name='Название компании', max_length=255)
    logo=models.ImageField(verbose_name='Логотип компании')
    
    class Meta:
        verbose_name='Наш клиент'
        verbose_name_plural='Наши клиенты'

    def __str__(self) -> str:
        return self.title

class Contacts(models.Model):
    whatsapp=models.URLField(verbose_name='Ссылка на WhatsApp',null=True,blank=True)
    telegram=models.URLField(verbose_name='Ссылка на Telegram',null=True,blank=True)

    class Meta:
        verbose_name='Контакты'
        verbose_name_plural='Контакты'

    def __str__(self) -> str:
        return "Контакты"
# Create your models here.
