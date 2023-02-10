from django.shortcuts import render
from django.utils import timezone
from .models import Post 
#the dot before models means current directory or current application, so we didn't need to mention .py


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

