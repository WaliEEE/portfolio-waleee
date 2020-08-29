from django.db import models

class Blog(models.Model):

	 title = models.CharField(max_length=30)
	 date  = models.DateTimeField()
	 Blog  = models.TextField()
	 image = models.ImageField(upload_to='images/')
