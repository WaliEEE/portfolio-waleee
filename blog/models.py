from django.db import models
from django.db.models import Model

class Blog(models.Model):

	title  = models.CharField(max_length=255, null=True)
	pub_date = models.DateTimeField(null=True)
	image   = models.ImageField(upload_to='images/', null=True)
	summary = models.TextField(max_length=5000, null=True)

	