from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save

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


class ChekTest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    finded_question = models.PositiveIntegerField(default=0)
    user_passed = models.BooleanField(default=False)
    percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.student)


class ChekQuestion(models.Model):
    checktest = models.ForeignKey(ChekTest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    given_answer = models.CharField(max_length=1, help_text='Например: A')
    true_answer = models.CharField(max_length=1, help_text='Например: A')
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return str(self.checktest)


@receiver(pre_save, sender=ChekQuestion)
def chek_answer(sender, instance, *args, **kwargs):
    if instance.given_answer == instance.true_answer:
        instance.is_true = True


@receiver(pre_save, sender=ChekTest)
def chek_test(sender, instance, *args, **kwargs):
    chektest = instance
    chektest.finded_question = ChekQuestion.objects.filter(checktest=chektest, is_true=True).count()
    print(chektest.finded_question)
    try:
        chektest.percentage = int(chektest.finded_question) * 100 // ChekQuestion.objects.filter(checktest=chektest).count()
        if chektest.test.percentage <= chektest.percentage:
            chektest.user_passed = True
    except:
        pass
