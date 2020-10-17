from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    class Meta:
        verbose_name_plural = "Subjects"
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=100, null=True)
    subject = models.ForeignKey(Subject, related_name="subjects", on_delete=models.CASCADE, null=True)
    select = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    result = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, related_name="questions", on_delete=models.CASCADE, null=True)
    answer  = models.ForeignKey(Choice, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)
