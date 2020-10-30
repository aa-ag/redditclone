from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models


@login_required(login_url='/account/login/')
def create(request):
    '''
    View from home to create posts
    '''
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            # TO DO: validate URL's / regex
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            context = {'error': 'You must include a title AND a URL ;)'}
            return render(request, 'posts/create.html', context)
    else:
        return render(request, 'posts/create.html')


def home(request):
    '''
    Home view for logged-in users
    '''
    posts = models.Post.objects.order_by('votes_total')
    context = {'posts': posts}
    return render(request, 'posts/home.html', context)


def upvote(request, pk):
    '''
    View to increase total votes
    '''
    if request.method == 'POST':
        post = models.Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home')


def downvote(request, pk):
    '''
    View to decrease total votes
    '''
    if request.method == 'POST':
        post = models.Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('home')