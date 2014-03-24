from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	profile_website = models.URLField(max_length=300, blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __unicode__(self):
		return self.user.username

class Company(models.Model):
	name = models.CharField(max_length=100, unique=True)
	website = models.URLField(max_length=300, blank=True)

	def __unicode__(self):
		return self.name

class Job(models.Model):
	company = models.ForeignKey(Company)
	title = models.CharField(max_length=100, verbose_name="Job Title")
	location = models.CharField(max_length=100, blank=True)
	description = models.CharField(max_length=1000, verbose_name="Job Description")
	salary = models.PositiveIntegerField(null=True, blank=True)
	job_website = models.URLField(max_length=300, blank=True)
	posted_date = models.DateField(null=True, blank=True)
	deadline = models.DateField(null=True, blank=True, verbose_name="Application Deadline")
	created = models.DateField(auto_now_add=True)
	lasted_modified = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.title
