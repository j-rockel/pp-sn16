from django.db import models
from django.utils import timezone
from django.conf import settings

image1= models.ImageField(upload_to=settings.MEDIA_ROOT)

class Todo(models.Model): 
	content = models.CharField(max_length=160)
	deadline = models.DateField(default=timezone.now)
	progress = models.FloatField()

	def create(self):
		self.save()

	def edit(self):
		self.save()

	def remove(self):
		self.save()