from django.contrib import admin

from applications.post.models import Post, Comment, Category, Rating, Like, Image


class ImageAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin
    ]
    list_display = ['title', 'likes']

    @staticmethod
    def likes(obj):
        return obj.likes.filter(like=True).count()


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Rating)
