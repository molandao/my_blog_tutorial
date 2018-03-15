from django.db import models

from django.db.models import permalink
# decase url code

# Create your models here.

class Blogpost(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    author = models.CharField(max_length = 100, unique = True)
    slug = models.SlugField(max_length = 100, unique = True) 
    body = models.TextField() #content
    posted = models.DateField(db_index = True, auto_now_add = True) # date_time

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug }) # auto

    class Meta: 
        ordering = ['-posted']
