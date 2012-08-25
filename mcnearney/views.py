from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import ContactForm

def home(request):
	return HttpResponseRedirect(reverse('blog.views.post_list'))
	
def contact(request, sent=None):
	# This view supports both normal postback and AJAX submitting
	
	def render(template, variables):
		# Renders the template with the specified variables
		return render_to_response(template, variables, context_instance=RequestContext(request))
		
	def send_mail(form):
		# Sends the validated form and returns if it was sent successfully
		sender = '%(name)s <%(email)s>' % \
			{'name': form.cleaned_data['sender_name'],
			 'email': form.cleaned_data['sender_email'],}
		subject = 'Website E-mail: %s' % form.cleaned_data['subject']
		message = form.cleaned_data['message']
		recipients = ['Lance McNearney <lance@mcnearney.net>']
		
		email = EmailMessage(subject, message, sender, recipients,
			headers = {'Reply-To': sender})
		
		try:
			email.send()
			return True
		except:
			return False
	
	# Normal template and empty form
	template = 'contact.django.html'
	form = ContactForm()
	
	# Ajax template
	if request.is_ajax():
		template = 'contact.form.django.html'
	
	# Catch re-direct and render thank you message
	if sent is not None:
		return render(template, locals())
	
	# Send the e-mail if it is valid
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			if send_mail(form):
				sent = True
				form = ContactForm()
				if not request.is_ajax():
					return HttpResponseRedirect(reverse('views.contact', kwargs={'sent': 'thanks'}))
			else:
				failed = True
		
	return render(template, locals())