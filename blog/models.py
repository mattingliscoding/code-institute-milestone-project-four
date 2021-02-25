from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    category = models.CharField(max_length=254)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,
                                      verbose_name='post_created_date')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}'.format(self.title,
                               self.category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)
