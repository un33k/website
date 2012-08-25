from django.contrib import admin
from blog.models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
 
class FileInline(admin.TabularInline):
    model = File
    extra = 1
    
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [FileInline, ImageInline]
    list_display = ('title', 'publish')
    list_filter = ('publish', 'categories')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)