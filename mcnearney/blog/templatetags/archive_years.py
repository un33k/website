from django.template import Library, Node, TemplateSyntaxError
from blog.models import Post

register = Library()

class ArchiveYears(Node):	
	def __init__(self, count, varname):
		self.count = int(count)
		self.varname = varname
		
	def render(self, context):
		try:
			context[self.varname] = Post.objects.published().dates('publish', 'year', order='DESC')[:self.count]
		except:
			context[self.varname] = None			
		return ''

@register.tag
def archive_years(parser, token):
	'''
	Returns a list of the most recent years that contain posts.
	
	Usage::
		{% archive_years 2 as years %}
	'''
	bits = token.contents.split()
	if len(bits) != 4:
		raise TemplateSyntaxError, 'archive_years takes exactly three arguments'
	if bits[2] != 'as':
		raise TemplateSyntaxError, 'second argument must be "as"'
	return ArchiveYears(bits[1], bits[3])