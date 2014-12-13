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

PAGE_TYPE = (
	('ABOUT', 'About Page'),
	('CONTACT', 'Contact Page'),
)


class Page(MPTTModel):
	name = models.CharField(max_length=200, unique=True, verbose_name="Page")
	parent = TreeForeignKey("self", null=True, blank=True, related_name="childern", verbose_name="Parent", help_text="Leave it empty if your menu is going to be root menu")
	author = models.ForeignKey(User, null=True, blank=True)
	content = models.TextField(null=True, blank=True, verbose_name="Post page content")
	permalink = models.SlugField(blank=True, verbose_name="URL Link", db_index=True, help_text="url link in format alphabet only without http://,")
	menu = models.CharField(max_length=18, choices=MENU_CHOICES, verbose_name="Assigned To Menu", help_text="Set this link to head, side or \
		bottom within your page")
	pub_date = models.DateField(verbose_name="Published Date")
	pub_status = models.BooleanField(verbose_name="Published")
	modified_date = models.DateTimeField(auto_now=True)
	page_type = models.CharField(max_length=10, verbose_name="Page Type", choices=PAGE_TYPE, null=True, blank=True)
	order = models.IntegerField(null=True, blank=True)

	class MPTTMeta:
		order_insertion_by = ['order']

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.permalink:
			if self.is_child_node():
				self.permalink = self.parent.permalink + "/" + slugify(self.name)
			else:
				self.permalink = slugify(self.name)

		super(Page, self).save(*args, **kwargs)

	def get_absolute_url(self):
		# Handle script prefix manually because we bypass reverse()
		return iri_to_uri("http://127.0.0.1:8000/%s" % self.permalink)
