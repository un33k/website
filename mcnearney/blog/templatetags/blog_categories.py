from django.template import Library, Node, TemplateSyntaxError
from blog.models import Category

register = Library()

class BlogCategories(Node):	
	def __init__(self, varname):
		self.varname = varname
		
	def render(self, context):
		try:
			context[self.varname] = Category.objects.all().exclude(post__isnull=True)
		except:
			context[self.varname] = None			
		return ''

@register.tag
def blog_categories(parser, token):
	'''
	Returns all of the blog categories.
	
	Usage::
		{% blog_categories as categories %}
	'''
	bits = token.contents.split()
	if len(bits) != 3:
		raise TemplateSyntaxError, 'blog_categories takes exactly three arguments'
	if bits[1] != 'as':
		raise TemplateSyntaxError, 'second argument must be "as"'
	return BlogCategories(bits[2])