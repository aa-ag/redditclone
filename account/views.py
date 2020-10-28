from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

def signup(request):
    '''
    Renders view where users complete form to sign up
    '''
    if request.method == 'POST':
        User.objects.create_user(request.POST['username'], password=request.POST['password'])
        return render(request, 'account/signup.html')
    else:
        return render(request, 'account/signup.html')
