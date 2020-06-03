from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	thumb = models.ImageField(upload_to='media/images',blank=True)
	


def __str__(self):
	return self.title
	