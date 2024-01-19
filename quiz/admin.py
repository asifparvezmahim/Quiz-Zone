from django.contrib import admin
from .models import Question, UserSubmittedAnswer


# Register your models here.
admin.site.register(Question)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "user", "given_answer"]


admin.site.register(UserSubmittedAnswer, UserSubmittedAnswerAdmin)
