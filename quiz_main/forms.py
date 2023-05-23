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

    submit_and_exit = forms.BooleanField(required=False)

    def save(self, test_id, commit=True):
        question = self.instance
        question.test = Test.objects.get(id=test_id)
        super().save(commit)
        return question
