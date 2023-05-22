from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    ''' Класс Категорий, нужен для добавления категориев.
     Принимает один обьязательный отрибут при создании name '''
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Test(models.Model):
    ''' Клас для создания тестов.
        Принимает 7 обьязательных атрибута, имя юзера, категория теста, заголовок теста, макс-попытки, дата-начала,
        дата-конца и процент прохода '''

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    max_attempts = models.PositiveIntegerField(default=1)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=10))
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Question(models.Model):
    ''' Класс для создания вопросов и ответов '''

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    T = models.CharField(max_length=200, help_text='НАПРИМЕР: A')

    def __str__(self):
        return str(self.question[:100])
