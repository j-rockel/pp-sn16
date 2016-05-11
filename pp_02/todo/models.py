from django.db import models
from django.utils import timezone

class Todo(models.Model): 
	content = models.CharField(max_length=160)
	deadline = models.DateTimeField(blank=True)			#was muss da noch rein? 
	progress = models.FloatField()

	def create(self):
		self.save()

	def edit(self):
		self.save()

	def remove(self):
		self.save()