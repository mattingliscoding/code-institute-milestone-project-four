from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    category = models.CharField(max_length=254)
    content = models.TextField()
    created_on = models.DateTimeField('blog_posted_date')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}'.format(self.title,
                               self.category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


class BlogImage(models.Model):
    image = models.ImageField(null=False)
    article_id = models.ForeignKey('BlogPost', null=True,
                                   blank=True, on_delete=models.SET_NULL,
                                   verbose_name='image_article_id')

    def __str__(self):
        return '{}, {}'.format(self.image,
                               self.article_id)


class BlogComment(models.Model):
    article_id = models.ForeignKey('BlogPost', null=True,
                                   related_name="comments", blank=True,
                                   on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True,
                                blank=True, on_delete=models.SET_NULL)
    comment_title = models.CharField(max_length=50)
    comment = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True,
                                      verbose_name='comment_posted_date')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}, {}'.format(self.article_id,
                                   self.user_id,
                                   self.comment_title)
