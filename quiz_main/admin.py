from django.contrib import admin
from .models import Category, Question, Test, ChekTest, ChekQuestion


# Register your models here.

class QuestionInline(admin.TabularInline):
    model = Question


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'author']


admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Test, TestAdmin)

admin.site.register(ChekTest)
admin.site.register(ChekQuestion)
