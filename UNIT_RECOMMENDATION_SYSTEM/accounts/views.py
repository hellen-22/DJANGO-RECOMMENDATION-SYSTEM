from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.models import auth

def signup(request):
    
    if request.method == 'POST':
        registration_number = request.POST['registration_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if CustomUser.objects.filter(registration_number=registration_number).exists():
                messages.info(request, 'Registration Number Is Already taken')
                return redirect('signup')

            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')

            else:
                user = CustomUser.objects.create_user(registration_number=registration_number, email=email, password=password)
                user.is_active = False
                user.save()
                return redirect('home')

        else:
            messages.info(request, 'Password Does not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')