from django.template import Library, Node, TemplateSyntaxError
from blog.models import Post

register = Library()

class RecentPosts(Node):	
	def __init__(self, count, varname):
		self.count = int(count)
		self.varname = varname
		
	def render(self, context):
		try:
			context[self.varname] = Post.objects.published()[:self.count]
		except:
			context[self.varname] = None			
		return ''

@register.tag
def recent_posts(parser, token):
	'''
	Returns the specified number of most recent posts.
	
	Usage::
		{% recent_posts 10 as recent %}
	'''
	bits = token.contents.split()
	if len(bits) != 4:
		raise TemplateSyntaxError, 'recent_posts takes exactly three arguments'
	if bits[2] != 'as':
		raise TemplateSyntaxError, 'second argument must be "as"'
	return RecentPosts(bits[1], bits[3])