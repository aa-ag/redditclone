from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models


@login_required(login_url='/account/login/')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            # TO DO: validate URL's / regex
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return render(request, 'posts/home.html')
        else:
            context = {'error': 'You must include a title AND a URL ;)'}
            return render(request, 'posts/create.html', context)
    else:
        return render(request, 'posts/create.html')


def home(request):
    return render(request, 'posts/home.html')