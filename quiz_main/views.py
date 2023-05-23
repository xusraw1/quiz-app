from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Test, Question, ChekTest, ChekQuestion
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone


@login_required(login_url='login')
def test(request, pk):
    test = get_object_or_404(Test, id=pk)
    attempts = ChekTest.objects.filter(student=request.user, test=test).count()
    if (timezone.now() >= test.start_date and timezone.now() <= test.end_time) and attempts < test.max_attempts:
        questions = Question.objects.filter(test=test)
        if request.method == 'POST':
            checktest = ChekTest.objects.create(student=request.user, test=test)
            for question in questions:
                given_answer = request.POST[str(question.id)]
                ChekQuestion.objects.create(checktest=checktest, question=question, given_answer=given_answer,
                                            true_answer=question.T)
            checktest.save()
            return redirect('checktest', checktest.id)

        context = {
            'question': questions,
            'test': test,

        }
        return render(request, 'test.html', context)
    else:
        return HttpResponse("Тест не найден")


@login_required(login_url='login')
def chek_test(request, pk):
    checktest = get_object_or_404(ChekTest, id=pk, student=request.user)
    return render(request, 'checktest.html', {'checktest': checktest})


@login_required(login_url='login')
def ready_to_test(request, pk):
    test = get_object_or_404(Test, id=pk)
    return render(request, 'ready_to_test.html', {'test': test})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'registration/sign_up.html', {'form': form})


def index(request):
    tests = Test.objects.all()
    return render(request, 'index.html', {'tests': tests})


from .forms import TestForm, QuestionForm


@login_required(login_url='login')
def new_test(req):
    form = TestForm()
    if req.method == 'POST':
        form = TestForm(req.POST)
        if form.is_valid():
            test_id = form.save(req)
            return redirect('new_question', test_id)
    return render(req, 'newtest.html', {'form': form})


@login_required(login_url='login')
def new_question(req, test_id):
    test = get_object_or_404(Test, id=test_id)
    if test.author == req.user:
        form = QuestionForm()
        if req.method == 'POST':
            form = QuestionForm(req.POST)
            if form.is_valid():
                form.save(test_id)
                if form.cleaned_data['submit_and_exit']:
                    return redirect('profile', req.user.id)
                return redirect('new_question', test_id)
        return render(req, 'newquestion.html', {'form': form, 'test': test})
    else:
        return HttpResponse("Что то пошло не так!!!")


@login_required(login_url='login')
def profile(req, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(req, 'profile.html', {'user': user})
