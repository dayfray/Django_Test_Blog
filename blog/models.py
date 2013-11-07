from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	pub_date = models.DateTimeField()
	tags = TaggableManager()

	def __unicode__(self):
		return self.title
