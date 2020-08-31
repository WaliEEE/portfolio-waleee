from django.db import models
from django.db.models import Model

class Blog(models.Model):

	image   = models.ImageField(upload_to='images/',null=True)
	summary = models.TextField(max_length=5000, null=True)

	