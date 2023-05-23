from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Test, Question
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def test(request, pk):
    test = get_object_or_404(Test, id=pk)
    questions = Question.objects.filter(test=test)
    if request.method == 'POST':
        for question in questions:
            given_answer = request.POST[str(question.id)]
            print(given_answer)
            if question.T == given_answer:
                print(True)
            else:
                print(False)
    context = {
        'question': questions,
        'test': test,

    }
    return render(request, 'test.html', context)


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
