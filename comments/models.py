from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from content.models import Post

# Create your models here.

class Comment(MPTTModel):
	post = models.ForeignKey(Post, verbose_name="Post")
	content = models.TextField(verbose_name="Comment")
	parent = TreeForeignKey('self', null=True, blank=True)
	author = models.CharField(max_length=50, null=True, blank=True)
	date = models.DateField(auto_now=True)
	status = models.BooleanField(default=False, verbose_name="Published")

	def __unicode__(self):
		return self.author

	class MPTTMeta:
		order_insertion_by = ['date']
