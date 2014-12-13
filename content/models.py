from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from pages.models import Page
from django.core.urlresolvers import reverse

# Create your models here.
#

COMMENT_ALLOWED_STATUS = (
	('ALLOWED', 'Open for comments'),
	('DISABLED', 'Close comments for this post'),
)

class Tag(models.Model):
	name = models.CharField(max_length=100, verbose_name="Tag")

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name="Categories")
	description = models.TextField()
	class Meta:
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name="Title")
	permalink = models.SlugField(verbose_name="Post URL Link")
	content = models.TextField()
	author = models.ForeignKey(User, null=True, blank=True)
	pub_date = models.DateField(verbose_name="Date Published")
	modified_date = models.DateField(auto_now=True, verbose_name="Date Modified")
	tag = models.ManyToManyField(Tag, blank=True, verbose_name="Post Tag", help_text="Put multiple tag separated with commas Example: \'computer, news, blog\'")
	category = models.ManyToManyField(Category, blank=True, verbose_name="Category")
	pub_status = models.BooleanField(verbose_name="Published")
	comments_status = models.CharField(max_length=20, choices=COMMENT_ALLOWED_STATUS, verbose_name="Comments Status")
	comments_count = models.BigIntegerField(blank=True, null=True, verbose_name="Comments Count")

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			if not self.permalink:
				self.permalink = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def get_absolute_url(self):
		from content import views
		return reverse(views.single_post)