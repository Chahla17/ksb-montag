from django.db import models

class Service(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка', max_length=50, default='fa-shield-alt')
    price = models.CharField('Цена', max_length=100, blank=True)
    order = models.IntegerField('Порядок', default=0)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    client = models.CharField('Клиент', max_length=200, blank=True)
    
    def __str__(self):
        return self.title

from django.db import models

class Service(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка', max_length=50, default='fa-shield-alt')
    price = models.CharField('Цена', max_length=100, blank=True)
    order = models.IntegerField('Порядок', default=0)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    client = models.CharField('Клиент', max_length=200, blank=True)
    
    def __str__(self):
        return self.title

# ДОБАВЬТЕ ЭТУ МОДЕЛЬ
class Request(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    message = models.TextField('Сообщение', blank=True)
    created_at = models.DateTimeField('Дата отправки', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)
    
    def __str__(self):
        return f"{self.name} - {self.phone}"
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']