from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.contrib.comments.moderation import CommentModerator, moderator
from blog.managers import PublicManager
from sorl.thumbnail.fields import ImageWithThumbnailsField
from markdown import markdown
import datetime

class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('title',)
        
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('blog_category_detail', None, {'slug': self.slug})
            
class Post(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique_for_date='publish')
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True, null=True)
    publish = models.DateTimeField(default=datetime.datetime.now)
    allow_comments = models.BooleanField(default=True)
    created = models.DateTimeField(editable=False, default=datetime.datetime.now)
    modified = models.DateTimeField(editable=False, auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    objects = PublicManager()
    
    def save(self):
        self.body_html = markdown(self.body, ['codehilite'])
        super(Post, self).save()
    
    class Meta:
        ordering = ('-publish',)
        get_latest_by = 'publish'
        
    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('blog_detail', None, {
            'year': self.publish.year,
            'month': self.publish.month,
            'day': self.publish.day,
            'slug': self.slug
        })
        
    def get_previous_post(self):
        return self.get_previous_by_publish()
    
    def get_next_post(self):
        return self.get_next_by_publish()
    
from django.db.models.signals import post_delete, post_save
from urllib2 import urlopen

NGINX_PURGE_PREFIX = '/purge'

def purge_nginx_cache(instance, **kwargs):
    '''
    Purges the Nginx cache whenever a Post is saved or deleted
    '''
    # This can't be tested using the built-in development server because it
    # can only handle one request at a time.
    if settings.DEBUG:
        print 'Purge Nginx Cache: %s' % instance.get_absolute_url()
        return
    
    # Send request to Nginx to purge the cache using specified prefix
    try:
        url = '%s%s%s' % (settings.BASE_URL, NGINX_PURGE_PREFIX, instance.get_absolute_url())
        urlopen(url)
    except:
        pass
    
post_save.connect(purge_nginx_cache, sender=Post)
post_delete.connect(purge_nginx_cache, sender=Post)

class PostModerator(CommentModerator):
    auto_close_field = 'publish'
    close_after = 90
    email_notification = True
    enable_field = 'allow_comments'
    
    def moderate(self, comment, content_object, request):
        return True

moderator.register(Post, PostModerator)

class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images')
    width = models.PositiveIntegerField(editable=False)
    height = models.PositiveIntegerField(editable=False)
    image = models.ImageField(
        upload_to='blog/images',
        width_field='width',
        height_field='height'
    )
    
class File(models.Model):
    post = models.ForeignKey(Post, related_name='files')
    file = models.FileField(
        upload_to='blog/files'
    )