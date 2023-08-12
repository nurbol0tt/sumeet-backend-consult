from django.contrib import admin

from apps.answersage.models import Question, Answer

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
