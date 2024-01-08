from django.contrib import admin
from .models import Release, Category

admin.site.register(Release)
admin.site.register(Category)

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
