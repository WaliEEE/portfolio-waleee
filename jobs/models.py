from django.db import models
from django.db.models import Model

class Job(models.Model):

	image = models.ImageField(upload_to='images/',null=True)




