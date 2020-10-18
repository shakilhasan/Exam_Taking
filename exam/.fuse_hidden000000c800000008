from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.core.mail import send_mail

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.forms.models import model_to_dict
from .models import Subject
from .models import Choice
from .models import Question
from .models import Submission
from .forms import SubjectForm
from .forms import ChoiceForm
from .forms import QuestionForm
from .forms import SubmissionForm
from .serializers import QuestionSerializer
from .serializers import SubmissionSerializer
# Create your views here.
#...........api start.........................
def question_api(request):
    template = loader.get_template('exam/question_api.html')
    context = {}
    return HttpResponse(template.render(context, request))

@api_view(['GET', 'POST'])
def question_collection(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        data = {'name': request.data.get('the_post')}
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def question_element(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#...........api end.........................
#...........subject start....................
def subject_add(request):
    template = loader.get_template('exam/subject_add.html')
    if request.user.is_superuser:
        if request.method == 'POST':
            form = SubjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('subject_add')
        else :
            form = SubjectForm
        context = {'form':form}
        return HttpResponse(template.render(context, request))

def subject_home(request):
    template = loader.get_template('exam/subject_home.html')
    subject = Subject.objects.all()
    context = {'subject':subject}
    return HttpResponse(template.render(context, request))

def subject_detail(request,subject_id):
    template = loader.get_template('exam/question_home.html')
    subject = Subject.objects.get(id=subject_id)
    question = Question.objects.filter(subject=subject)
    choices = Choice.objects.order_by('?')
    context = {
    'question':question,
    'choices':choices,
    }
    return HttpResponse(template.render(context, request))
#...........subject end....................

#...........question start....................
def question_add(request):
    template = loader.get_template('exam/question_add.html')
    if request.user.is_superuser:
        if request.method == 'POST':
            form = QuestionForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save()
                choice_name=[]
                choice_name.append(request.POST.get('choice1'))
                choice_name.append(request.POST.get('choice2'))
                choice_name.append(request.POST.get('choice3'))
                choice_name.append(request.POST.get('choice4'))
                answer_name=request.POST.get('answer' )
                for name in choice_name:
                    if name:
                        data = { 'question':obj, 'name':name, }
                        cform=Choice(**data)
                        cform.save()
                data = { 'question':obj, 'name':answer_name, 'result':True }
                cform=Choice(**data)
                cform.save()
                return redirect('question_add')
        else:
            form = QuestionForm
            choices= Choice.objects.all()
        context = {'form':form, 'choices':choices}
        return HttpResponse(template.render(context, request))

def question_home(request):
    template = loader.get_template('exam/question_home.html')
    if request.method == 'POST':
        question = Question.objects.filter(name__contains=request.POST.get('search'));
    else:
        question = Question.objects.order_by('?')
    choices = Choice.objects.order_by('?')
    context = { 'question' : question , 'choices':choices }
    return HttpResponse(template.render(context, request))

def question_edit(request,question_id):
    template = loader.get_template('exam/question_edit.html')
    if request.user.is_superuser:
        question = Question.objects.get(id=question_id)
        choices=  Choice.objects.filter(question=question)
        if request.method == 'POST':
            form = QuestionForm(request.POST, request.FILES, instance=question)
            if form.is_valid():
                form.save()
            for choice in choices:
                obj=choice
                obj.name=request.POST.get(str(choice.id))
                obj.save()
            return redirect('question_home')
        else:
            form = QuestionForm(instance=question)
        context = {'form':form, 'choices':choices}
        return HttpResponse(template.render(context, request))

def question_delete(request,question_id):
    if request.user.is_superuser:
        questions = Question.objects.get(id=question_id)
        questions.delete()
        return redirect('question_home')
#...........question end....................
#...........submission start....................
# @login_required(login_url='/login/')
def submission_add(request):
    if request.user.is_authenticated:
        name= request.user.username
        u= User.objects.get(username=name)
    #if request.method == 'POST':
    question_id = request.POST.get('question_id')
    choice_id= request.POST.get('choice')
    question = Question.objects.get(id=question_id)
    answer = Choice.objects.get(id=choice_id)
    data = {
     'user':u,
     'question':question,
     'answer':answer,
      }
    send_mail(
    'submitted by '+str(name),
    'question: '+str(json.dumps(model_to_dict(question)))+
    '\n\nanswer: '+str(json.dumps(model_to_dict(answer))),
    'student@example.com',
    ['shakilhasan105268@gmail.com','teacher@example.com','head@example.com'],
    fail_silently=True,
    )
    form=Submission(**data)
    form.save()
    return redirect('question_home')

def submission_home(request):
    template = loader.get_template('exam/submission_home.html')
    submissions = Submission.objects.all();
    context = { 'submissions' : submissions }
    return HttpResponse(template.render(context, request))

def submission_delete(request,submission_id):
    if request.user.is_superuser:
        submission = Submission.objects.get(id=submission_id)
        submission.delete()
        return redirect('submission_home')
#...........submission end....................
