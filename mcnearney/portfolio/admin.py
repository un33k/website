from portfolio.models import *
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'order',)
	list_editable = ('order',)
	
admin.site.register(Category, CategoryAdmin)
	
class ThumbnailInline(admin.TabularInline):
	model = Thumbnail
	extra = 5
	
class VideoInline(admin.StackedInline):
	model = Video
	extra = 1
	prepopulated_fields = {'slug': ('title',)}

class ProjectAdmin(admin.ModelAdmin):
	inlines = [VideoInline, ThumbnailInline]
	list_display = ('title', 'start_date', 'end_date', 'team_size', 'category', 'published',)
	list_editable = ('start_date', 'end_date', 'team_size', 'category', 'published',)
	prepopulated_fields = {'slug': ('title',)}
	
admin.site.register(Project, ProjectAdmin)