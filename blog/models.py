from django.db import models
from django.db.models import Model

class Blog(models.Model):

	title  = models.CharField(max_length=255, null=True)
	pub_date = models.DateTimeField(null=True)
	image   = models.ImageField(upload_to='images/', null=True)
	summary = models.TextField(max_length=5000, null=True)


	def __str__(self):
		return self.title

	def body(self):
		return self.summary[:100]

	def date(self):
		return self.pub_date.strftime('%b %e , %Y')