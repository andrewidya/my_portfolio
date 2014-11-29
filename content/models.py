from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=100, verbose_name="Tag")

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name="Title")
	slug_title = models.SlugField(verbose_name="Slug")
	content = models.TextField()
	author = models.ForeignKey(User)
	pub_date = models.DateTimeField(verbose_name="Date Published")
	modified_date = models.DateTimeField(auto_now=True, verbose_name="Modified")
	tag = models.ManyToManyField(Tag, blank=True)
	pub_status = models.BooleanField(verbose_name="Published")

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug_title = slugify(self.title)

		super(Post, self).save(*args, **kwargs)