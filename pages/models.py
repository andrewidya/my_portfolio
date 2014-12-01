from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify
from django.utils.encoding import iri_to_uri

# Create your models here.

class Page(MPTTModel):
	name = models.CharField(max_length=200, unique=True, verbose_name="Page")
	parent = TreeForeignKey("self", null=True, blank=True, related_name="childern", verbose_name="Parent")
	author = models.ForeignKey(User)
	permalink = models.SlugField(verbose_name="Url Link", db_index=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			if self.is_child_node():
				self.permalink = self.parent.permalink + "/" + slugify(self.name)
			else:
				self.permalink = slugify(self.name)

		super(Page, self).save(*args, **kwargs)

	class MPTTMeta:
		order_insertion_by = ['name']

	def get_absolute_url(self):
		# Handle script prefix manually because we bypass reverse()
		return iri_to_uri(get_script_prefix().rstrip('/') + self.permalink)
