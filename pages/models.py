from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Post(models.Model):
	CATAGORY_CHOICES = (
		
		('T','Technology'),
		('E','Socio/Econ'),

	)
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=1, choices=CATAGORY_CHOICES)
	photo = models.ImageField(upload_to='postimages')
	intro = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	video = EmbedVideoField(blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

class Subscription(models.Model):
	name = models.CharField(max_length=100)
	email =models.EmailField()
	def __str__(self):
		return self.name

