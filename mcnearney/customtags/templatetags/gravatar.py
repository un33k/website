from django import template
from django.template import Library, Node, TemplateSyntaxError
import urllib, hashlib, httplib

register = Library()

GRAVATAR_DOMAIN = 'gravatar.com'
GRAVATAR_PATH = '/avatar/'

class GravatarNode(Node):   
    def __init__(self, email, size, varname):
        self.email = template.Variable(email)
        self.size = int(size)
        self.varname = varname
        
    def render(self, context):
        hash = hashlib.md5(self.email.resolve(context)).hexdigest()
        context[self.varname] = get_gravatar(hash, self.size)
        return ''
        
def is_default(hash):
    '''
    Returns whether the specified gravatar is returning the default icon.
    '''
    try:
        query = urllib.urlencode({
            'gravatar_id': hash,
            's': 1, # Smallest size available
            'default': '/' # Causes a re-direct when the gravatar is missing
        })
        full_path = '%s?%s' % (GRAVATAR_PATH, query)
        
        # Create connection and test for 302 redirect
        conn = httplib.HTTPConnection(GRAVATAR_DOMAIN)
        conn.request('HEAD', full_path)
        response = conn.getresponse()
        
        return response.status == 302
    except:
        return True
    
def get_gravatar(hash, size):
    '''
    Returns an object with the gravatar information.
    '''
    query = urllib.urlencode({
        'gravatar_id': hash,
        's': size
    })
    
    return {
        'src': 'http://%s%s?%s' % (GRAVATAR_DOMAIN, GRAVATAR_PATH, query),
        'width': size,
        'height': size,
        'is_default': is_default(hash)
    }   
    
@register.tag
def gravatar(parser, token):
    '''
    This tag is used for rendering a gravatar icon. You can also check that the gravatar exists by checking the is_default property.
        
    Usage::
        {% gravatar email_address size as variable_name %}
        
    Example::
        {% gravatar user.email 64 as icon %}
        {% if not icon.is_default %}
            <img src="{{ icon.src }}" width="{{ icon.width }}" height="{{ icon.height}}" alt=""/>
        {% endif %}
    '''
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, 'gravatar takes exactly four arguments'
    if bits[3] != 'as':
        raise TemplateSyntaxError, 'third argument must be "as"'
    return GravatarNode(bits[1], bits[2], bits[4])