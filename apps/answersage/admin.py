from django.contrib import admin

from apps.answersage.models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'consultant', 'topic', 'text', 'result', 'created'
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'question', 'answer', 'created'
    )
