from itertools import chain
from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField

class Category(models.Model):
	title = models.CharField(max_length=128)
	order = models.PositiveIntegerField(default=0, blank=False, null=False)
	
	class Meta:
		ordering = ['order']
		verbose_name_plural = 'categories'
	
	def __unicode__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=128)
	slug = models.SlugField()
	category = models.ForeignKey(Category)
	start_date = models.DateField()
	end_date = models.DateField(blank=True, null=True)
	url = models.URLField(blank=True, null=True, verify_exists=False)
	team_size = models.PositiveIntegerField(default=1, blank=False, null=False)
	summary = models.TextField()
	information = models.TextField(blank=True, null=True)
	published = models.BooleanField(default=False) 
	
	class Meta:
		ordering = ['-end_date']
	
	def __unicode__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('portfolio.views.detail', [self.slug])
		
	def year(self):
		'''
		Returns the year of the project depending on the end date.
		Examples:: 2008, 2008+, 2008 - 2009
		'''
		if self.end_date is None:
			return '%s+' % self.start_date.year	
		elif self.start_date.year != self.end_date.year:
			return '%s - %s' % (self.start_date.year, self.end_date.year)
		
		return self.start_date.year
	
	def get_previous_project(self):
		return self.get_previous_by_start_date(published=True, category=self.category)

	def get_next_project(self):
		return self.get_next_by_start_date(published=True, category=self.category)
		
	def videos_and_thumbnails(self):
		'''
		Returns all of the videos and thumbnails for this project in a single list.
		'''
		return list(chain(self.videos.all(), self.thumbnails.all()))

class Video(models.Model):
	project = models.ForeignKey(Project, related_name='videos')
	title = models.CharField(max_length=128, blank=False, null=False)
	slug = models.SlugField(db_index=False)
	summary = models.TextField(null=True, blank=True)
	video = models.FileField(upload_to='videos')
	thumbnail = ImageWithThumbnailsField(
		upload_to = 'videos/thumbnails',
		thumbnail = {'size' : (440, 330)},
	)
	width = models.PositiveIntegerField(blank=False, null=False)
	height = models.PositiveIntegerField(blank=False, null=False)
	order = models.PositiveIntegerField(default=0, blank=False, null=False)
	
	class Meta:
		ordering = ['order']
		unique_together = (('slug', 'project'),)
		
	def __unicode__(self):
		return '%s Video' % self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('portfolio.views.video', [self.project.slug, self.slug])

class Thumbnail(models.Model):
	project = models.ForeignKey(Project, related_name='thumbnails')
	title = models.CharField(max_length=128, blank=False, null=False)
	summary = models.TextField(null=True, blank=True)
	image = ImageWithThumbnailsField(
		upload_to = 'thumbnails',
		thumbnail = {'size' : (500, 375)},
	)
	order = models.PositiveIntegerField(default=0, blank=False, null=False)
	
	class Meta:
		ordering = ['order']
	
	def __unicode__(self):
		return self.title