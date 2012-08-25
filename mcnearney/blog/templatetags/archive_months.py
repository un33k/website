from django.template import Library, Node, TemplateSyntaxError
from blog.models import Post

register = Library()

class ArchiveMonths(Node):	
	def __init__(self, count, varname):
		self.count = int(count)
		self.varname = varname
		
	def render(self, context):
		try:
			context[self.varname] = Post.objects.published().dates('publish', 'month', order='DESC')[:self.count]
		except:
			context[self.varname] = None			
		return ''

@register.tag
def archive_months(parser, token):
	'''
	Returns a list of the most recent months that contain posts.
	
	Usage::
		{% archive_months 5 as months %}
	'''
	bits = token.contents.split()
	if len(bits) != 4:
		raise TemplateSyntaxError, 'archive_months takes exactly three arguments'
	if bits[2] != 'as':
		raise TemplateSyntaxError, 'second argument must be "as"'
	return ArchiveMonths(bits[1], bits[3])