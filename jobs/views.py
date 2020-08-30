from django.shortcuts import render
from .models import Job

def home(request):

	total_jobs = Job.objects

	return render(request, 'jobs/home.html', {'collection': total_jobs})
