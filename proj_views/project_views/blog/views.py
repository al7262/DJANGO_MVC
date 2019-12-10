from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {
        'isHome' : True
    })

def blog(request):
    return render(request, 'blog/blog.html', {
        'isBlog' : True
    })

def mentor(request):
    return render(request, 'blog/mentor.html', {
        'isMentor' : True
    })

def mentee(request):
    return render(request, 'blog/mentee.html', {
        'isMentee' : True
    })

def author(request):
    return render(request, 'blog/author.html', {
        'isAuthor' : True
    })