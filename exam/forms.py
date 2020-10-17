from django import forms
from .models import Subject
from .models import Choice
from .models import Question
from .models import Submission

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name','subject','select']
        # fields = '__all__'
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        # fields = ['cover','name','author','description','price','available','catagory']
        fields = '__all__'
