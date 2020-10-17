from django.contrib import admin
from .models import Subject
from .models import Choice
from .models import Question
from .models import Submission

# Register your models here.
admin.site.register(Subject)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Submission)
