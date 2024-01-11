from django.contrib import admin
from .models import Release, Category, Comment

admin.site.register(Release)
admin.site.register(Category)
admin.site.register(Comment)

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('release','text')
