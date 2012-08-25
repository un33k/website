from django.db.models import Manager
import datetime

class PublicManager(Manager):
	def published(self):
		''' Returns any published posts that are available. '''
		return self.get_query_set().filter(publish__lte=datetime.datetime.now())