from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegisterForm
from .models import MyUser
from django.contrib import auth


# Create your views here.

def user_registration(request):
    if request.user.is_authenticated:
        return HttpResponse('you are already logged in')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password != password2:
                context = {"error": "password did not match"}
                return render(request, 'accounts/register.html', context)
            form_data = {"email": email, "username": username, "password": password, "password2": password2, }
            form = UserRegisterForm(form_data)
            if form.is_valid():
                print('is_valid')
                user = MyUser(email=email, password=make_password(password), username=username)
                user.save()
                user = auth.authenticate(email=email, password=password)
                print(user)
                if user is not None:
                    auth.login(request, user)
                    return redirect('accounts:welcomepage')
                context = {"error": 'something went wrong'}
                return render(request, 'accounts/register.html', context)
            else:
                context = {"error": form.errors, "forms": UserRegisterForm()}
            print("error")
            return render(request, 'accounts/register.html', context)
    if request.method == 'GET':
        form = UserRegisterForm()
        context = {"forms": form}
        return render(request, 'accounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:welcomepage')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('accounts:welcomepage')
            else:
                context = {"errors": "User name or password is incorrect"}
                return render(request, 'accounts/login.html', context)
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('accounts:register')


@login_required
def welcomepage(request):
    return render(request, 'accounts/welcomepage.html')
