from django.db import models


class Request(models.Model):
    name=models.CharField(verbose_name="Имя",default='',max_length=255,null=True,blank=True)
    email=models.EmailField(verbose_name='Почта',null=True,blank=True)
    phone=models.CharField(verbose_name='Номер телефона',default='',null=True,blank=True,max_length=255)
    about=models.TextField(verbose_name='Описание',null=True,blank=True)

    class Meta:
        verbose_name='Заявка'
        verbose_name_plural='Заявки'
        
    def __str__(self) -> str:
        return f"Заявка №: {self.pk}"

# Create your models here.
