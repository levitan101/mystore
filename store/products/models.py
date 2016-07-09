from django.core.urlresolvers import reverse
from django.db import models
#from django.db.models.signals import post_save
#from django.utils.safestring import mark_safe
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	active = models.BooleanField(default=True)
	categories = models.ManyToManyField('Category', blank=True)
	default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)
	
	def __str__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.title
