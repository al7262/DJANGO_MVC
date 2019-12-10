from django.shortcuts import render
from .models import Mentor, Mentee, Blog

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {
        'isHome' : True
    })

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html', {
        'blogs': blog,
        'isBlog' : True
    })

def mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'blog/mentor.html', {
        'mentors' : mentor,
        'isMentor' : True
    })

def mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'blog/mentee.html', {
        'mentees': mentee,
        'isMentee' : True
    })

def author(request):
    return render(request, 'blog/author.html', {
        'isAuthor' : True
    })

def post(request):
    return render(request, 'blog/new_post.html', {
        'isPost' : True
    })

def posted(request):
    toBlog = Blog()
    toBlog.title = request.POST['title']
    toBlog.photo = request.POST['photo']
    toBlog.content = request.POST['content']
    toBlog.save()
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html', {
        'blogs': blog,
        'isPosted' : True,
        'isBlog': True
    })

def more(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog/more.html', {
        'blog': blog,
        'isMore' : True
    })