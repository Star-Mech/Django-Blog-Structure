from django.contrib import admin

from .models import Post, Category, Profile, Comment

# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'title_tag', 'author', 'body', 'pub_date')
#     list_filter = ['pub_date']
#     search_fields = ['body']
#
# admin.site.register(Post, PostAdmin)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)