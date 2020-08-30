from django.db import models
from django.db.models import Model

class Job(models.Model):

	image   = models.ImageField(upload_to='images/',null=True)
	summary = models.CharField(max_length=200, null=True)




