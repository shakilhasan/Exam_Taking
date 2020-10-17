from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.usignup, name='signup'),
    path('login/', views.ulogin, name='login'),
    path('logout/', views.ulogout, name='logout'),

    path('', include('exam.urls'), name='exam'),
]
