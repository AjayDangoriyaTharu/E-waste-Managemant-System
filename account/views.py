from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
# from account.models import contectEnquiry
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request, 'adminpage.html')


def customer(request):
    return render(request, 'index-3.html')


def employee(request):
    return render(request, 'employee.html')


def main(request):
    return render(request, 'index2.html')


def about(request):
    return render(request, 'about-us.html')


def service(request):
    return render(request, 'service.html')


def blog(request):
    return render(request, 'blog-classic.html')


def contact(request):
    return render(request, "contact.html")


def form(request):
    return render(request, "index-2.html")


def table(request):
    return render(request, "tables.html")

# server setup


# def saveEnquiry(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         objects = request.POST.get('object')
#         object_description = request.POST.get('object_descripytion')
#         en = contectEnquiry(name=name, email=email,
#                             phone=phone, address=address, objects=objects, object_description=object_description)
#         en.save()
#     return render(request, 'index-2.html')
