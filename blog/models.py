from django.db import models

from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=100)
    slug = models.SlugField(default ="",blank=False, null = False, unique=True, db_index=True)

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    title = models.TextField(max_length=100)
    description = RichTextField()
    publish_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="media")
    slug = models.SlugField(default ="",blank=False, null = False, unique=True, db_index=True)
    favourite = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
