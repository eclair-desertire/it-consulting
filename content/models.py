from django.db import models
from tinymce import models as tinymce_models
from django.utils import timezone

class Service(models.Model):
    title=models.CharField(verbose_name="Наименование услуги",max_length=255,default="")
    image=models.ImageField(verbose_name="Изображение услуги")
    description=models.TextField(verbose_name="Описание")
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name='Услуга'
        verbose_name_plural='Услуги'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f'/services/{self.pk}/'



class Portfolio(models.Model):
    title=models.CharField(verbose_name='Название проекта',max_length=255)
    client=models.CharField(verbose_name='Клиент',max_length=255,null=True,blank=True,default='')
    project_type=models.CharField(verbose_name='Тип проекта',max_length=255,default='')
    info=models.TextField(verbose_name='Информация о проекте',null=True,blank=True)
    portfolio_url=models.URLField(verbose_name="Ссылка на проект",blank=True,null=True)
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
    
class MainPageDigits(models.Model):
    clients=models.IntegerField(verbose_name='Обслужено клиентов',default=0)
    projects=models.IntegerField(verbose_name='Реализовано проектов',default=0)
    hours_of_support=models.IntegerField(verbose_name='Часов поддержки',default=0)
    hard_workers=models.IntegerField(verbose_name='Работников',default=0)

    class Meta:
        verbose_name='Цифры на главной'
        verbose_name_plural='Цифры на главной'

    def __str__(self) -> str:
        return "Цифры на главной: "+str(self.pk)

class Testimonal(models.Model):
    name=models.CharField(verbose_name='Имя',max_length=255,default='')
    company_models=models.CharField(verbose_name='Наименование компании',max_length=255,default='')
    testimonal=models.TextField(verbose_name='Отзыв')

    class Meta:
        verbose_name='Отзыв о нас'
        verbose_name_plural='Отзывы о нас'

    def __str__(self) -> str:
        return "Отзыв: "+str(self.pk)

class Contacts(models.Model):
    whatsapp=models.URLField(verbose_name='Ссылка на WhatsApp',null=True,blank=True)
    telegram=models.URLField(verbose_name='Ссылка на Telegram',null=True,blank=True)

    class Meta:
        verbose_name='Контакты'
        verbose_name_plural='Контакты'

    def __str__(self) -> str:
        return "Контакты"
# Create your models here.
