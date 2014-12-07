from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify
from django.utils.encoding import iri_to_uri
from django.core.urlresolvers import get_script_prefix

# Create your models here.
MENU_CHOICES = (
	('HEAD', 'Head Navigation'),
	('SIDE', 'Sidebar Navigation'),
	('BOTTOM', 'Bottom Navigation'),
)


class Page(MPTTModel):
	name = models.CharField(max_length=200, unique=True, verbose_name="Page")
	parent = TreeForeignKey("self", null=True, blank=True, related_name="childern", verbose_name="Parent", help_text="Leave it empty if your menu is going to be root menu")
	author = models.ForeignKey(User, null=True, blank=True)
	permalink = models.SlugField(verbose_name="Url Link", db_index=True)
	menu = models.CharField(max_length=18, choices=MENU_CHOICES, verbose_name="Assigned To Menu", help_text="Set this link to head, side or \
		bottom within your page")
	order_number = models.IntegerField(verbose_name="Order Priority", help_text="Set how your menu will ordered, put higher number \
		for top priority")

	class MPTTMeta:
		order_insertion_by = ['-order_number']

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			if self.is_child_node():
				self.permalink = self.parent.permalink + "/" + slugify(self.name)
			else:
				self.permalink = slugify(self.name)

		super(Page, self).save(*args, **kwargs)

	def get_absolute_url(self):
		# Handle script prefix manually because we bypass reverse()
		return iri_to_uri(get_script_prefix().rstrip('/') + self.permalink)
