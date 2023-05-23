from django import forms
from .models import Test, Question


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('title', 'category', 'max_attempts', 'end_time', 'percentage')

    def save(self, request, commit=True):
        test = self.instance
        test.author = request.user
        super().save(commit)
        return test.id


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'a', 'b', 'c', 'd', 'T')

    submit = forms.BooleanField(required=False)

    def save(self, request, commit=True):
        question = self.instance
        question.author = Test.objects.get(id=pk)
        super().save(commit)
        return question
