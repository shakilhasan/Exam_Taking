from rest_framework import serializers
from exam.models import Question
from exam.models import Submission


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        # fields = ['pk','name','author','description',]

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
        # fields = ['name']
