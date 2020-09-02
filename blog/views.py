from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    new_blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'collections':new_blogs})


def detail(request, blog_id):
    dblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':dblog})

