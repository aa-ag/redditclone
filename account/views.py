from django.shortcuts import render, HttpResponse

def signup(request):
    if request.method == 'POST':
        return HttpResponse("working")
    else:
        return render(request, 'account/signup.html')
