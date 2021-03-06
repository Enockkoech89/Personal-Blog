from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	p_image = models.ImageField(default='profile2.JPG', upload_to='profilepicsblog')
	biography = models.TextField(blank=True)

	def __str__(self):
		return f"{self.user.username} profile"