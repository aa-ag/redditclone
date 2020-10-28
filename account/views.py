from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

def signup(request):
    '''
    Renders view where users complete form to sign up
    '''
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordconfirmation']:
            User.objects.create_user(request.POST['username'], password=request.POST['password'])
            return render(request, 'account/signup.html')
        else:
            context = {'error': 'Passwords didn\'t match. Please try again.'}
            return render(request, 'account/signup.html', context)
    else:
        return render(request, 'account/signup.html')
