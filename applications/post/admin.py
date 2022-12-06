from django.contrib import admin

from applications.post.models import Post, Comment, Category


class AdminPost(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)