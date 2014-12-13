from django.contrib.auth.models import User
from django.db import models
from django.core.files import File
from django.conf import settings
from django.template.defaultfilters import slugify

from PIL import Image as PImage
from os.path import join
from tempfile import *
import os

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
	avatar_thumb = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
	street = models.CharField(max_length=500, blank=True, null=True, verbose_name="Address")
	city = models.CharField(max_length=50, blank=True, null=True, verbose_name="City")
	state = models.CharField(max_length=50, blank=True, null=True, verbose_name="State/Province")
	country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Country")
	about = models.TextField()

	def __unicode__(self):
		return self.user.get_username()

	def save(self, *args, **kwargs):
		super(UserProfile, self).save(*args, **kwargs)
		im = PImage.open(os.path.join(settings.MEDIA_ROOT, self.avatar.name))
		self.width, self.height = im.size

		filename, extension = os.path.splitext(self.avatar.name)
		im.thumbnail((50, 50), PImage.ANTIALIAS)
		thumb_file = filename + "-profile-thumbnail" + extension
		tf2 = NamedTemporaryFile()
		im.save(tf2.name, "JPEG")
		self.avatar_thumb.save(thumb_file, File(open(tf2.name)), save=False)
		tf2.close()

		super(UserProfile, self).save(*args, **kwargs)

	def thumbnail(self):
		return """<img alt="" src="/media/%s" />""" % (self.avatar_thumb.name)

	def user_name(self):
		return self.user.get_username()

	thumbnail.allow_tags = True