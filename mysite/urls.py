from django.urls import include, path
from django.shortcuts import render
from django.contrib import admin


def home(request):
    return render(request,'index2.html')

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('admin/clearcache/', include('clearcache.urls')),
    path('', include('account.urls')),

]