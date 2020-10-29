from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
    '''
    Renders view where users complete form to sign up:
    - Password and password confirmation must match. 
    - Username must be unique.
    '''
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordconfirmation']:
            try:
                user = User.objects.get(username=request.POST['username'])
                context = {'error': 'Username already in use.'}
                return render(request, 'account/signup.html', context)
            except User.DoesNotExist:

                user = User.objects.create_user(request.POST['username'], request.POST['email'], password=request.POST['password'])
                login(request, user)
                return render(request, 'account/signup.html')
        else:
            context = {'error': 'Passwords didn\'t match. Please try again.'}
            return render(request, 'account/signup.html', context)
    else:
        return render(request, 'account/signup.html')


def user_login(request):
    '''
    Renders view where users log into their account: 
    '''
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            context = {'message': 'Welcome!'}
            return render(request, 'account/login.html', context)
        else:
            context = {'error': 'Username or password didn\'t match. Please try again.'}
            return render(request, 'account/login.html', context)
    else:
        return render(request, 'account/login.html')
