from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    opt_1 = models.CharField(max_length=120)
    opt_2 = models.CharField(max_length=120)
    opt_3 = models.CharField(max_length=120)
    opt_4 = models.CharField(max_length=120)
    time = models.IntegerField()
    right_answer = models.CharField(max_length=120)  # quiz ans ekhane store korbo

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question


class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    given_answer = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "UserSubmittedAnswer"
