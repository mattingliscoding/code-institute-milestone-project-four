from django.contrib import admin
from .models import BlogPost, BlogComment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'category', 'created_on', 'image')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'comment_title', 'comment',
                    'created_on')
    search_fields = ['comment']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
