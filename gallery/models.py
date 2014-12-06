from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.files import File
from django.conf import settings

from PIL import Image as PImage
from os.path import join
from tempfile import *
import os

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'><img src='/media/%s' width='150'></a>" % (x, x) for x in lst]
        return ', '.join(lst)

    images.allow_tags = True


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tag

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=50)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    thumbnail2 = models.ImageField(upload_to="images/", blank=True, null=True)

    def __unicode__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(settings.MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size

        # large thumbnail
        fn, ext = os.path.splitext(self.image.name)
        im.thumbnail((50, 50), PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb2" + ext
        tf2 = NamedTemporaryFile()
        im.save(tf2.name, "JPEG")
        self.thumbnail2.save(thumb_fn, File(open(tf2.name)), save=False)
        tf2.close()

        super(Image, self).save(*args, ** kwargs)

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def tags_(self):
    	lst = [x.tag for x in self.tags.all()]
    	return ", ".join(lst)
    	lst = [x for x in Tag.objects.filter(image=self)]
    	return str(join(lst, ','))

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" width="150" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True