from django.template import Library, Node, TemplateSyntaxError
from django.utils import simplejson
import urllib

register = Library()

class StackOverflowUserNode(Node):	
	def __init__(self, userid, varname):
		self.userid = userid
		self.varname = varname
		
	def render(self, context):
		try:
			response = urllib.urlopen('http://stackoverflow.com/users/flair/%s.json' % self.userid).read()
			json = simplejson.loads(response)
			json['gravatarHtml'] = json['gravatarHtml'][:-1] + '/>' # Close img tag for valid xhtml
			context[self.varname] = json
		except:
			context[self.varname] = None			
		return ''

@register.tag
def get_stack_overflow_user(parser, token):
	'''
	This will return a JSON object with the specified Stack Overflow user's "flair" information.
	
	Usage::
		{% get_stack_overflow_user userid as variable_name %}
	'''
	bits = token.contents.split()
	if len(bits) != 4:
		raise TemplateSyntaxError, 'get_stack_overflow takes exactly three arguments'
	if bits[2] != 'as':
		raise TemplateSyntaxError, 'second argument must be "as"'
	return StackOverflowUserNode(bits[1], bits[3])