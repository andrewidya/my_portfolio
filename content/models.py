from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from pages.models import Page
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=100, verbose_name="Tag")

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name="Title")
	permalink = models.SlugField(verbose_name="Permalink")
	content = models.TextField()
	author = models.ForeignKey(User)
	pub_date = models.DateField(verbose_name="Date Published")
	modified_date = models.DateField(auto_now=True, verbose_name="Modified")
	tag = models.ManyToManyField(Tag, blank=True)
	pub_status = models.BooleanField(verbose_name="Published")
	page = models.ForeignKey(Page)

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.permalink = slugify(self.title)
		super(Post, self).save(*args, **kwargs)