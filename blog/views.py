from django.shortcuts import render

from .models import Blog

def allblogs(request):

	new_blogs = Blog.objects

	return render(request, 'blog/allblogs.html', {'collections':new_blogs})