from django.conf.urls import url
from . import  views
from django.urls import path, re_path



urlpatterns = [
    path('question_add/', views.question_add, name= 'question_add'),
    path('', views.question_home, name= 'question_home'),
    path('question_edit/<int:question_id>/', views.question_edit, name='question_edit'),
    path('question_delete/<int:question_id>/', views.question_delete, name='question_delete'),

    path('subject_add/', views.subject_add, name= 'subject_add'),
    path('subject_home/', views.subject_home, name='subject_home'),
    path('subject_detail/<int:subject_id>/', views.subject_detail, name='subject_detail'),

    path('submission_add/', views.submission_add, name= 'submission_add'),
    path('submission_home/', views.submission_home, name='submission_home'),
    path('submission_delete/<int:submission_id>/', views.submission_delete, name='submission_delete'),


# api
    path('question_api/api/v1/questions/',  views.question_collection, name= 'question_collection'),
    path('question_api/api/v1/questions/<int:pk>/', views.question_element, name='question_element'),
    path('question_api/', views.question_api ,name='question_api'),

 ]
