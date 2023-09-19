from django.urls import path
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [

    path('main', views.main, name='main'),
    path('loginpage', views.index, name='login'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    # path('saveform', views.saveEnquiry, name='saveform'),

]
