from django import forms
from django.contrib.comments.forms import CommentForm
from django.utils.safestring import mark_safe
from models import MarkdownComment

class MarkdownCommentForm(CommentForm):
	is_markdown = forms.BooleanField(label=mark_safe('Use <a href="http://en.wikipedia.org/wiki/Markdown">markdown</a> formatting (HTML is not allowed)'), required=False)
	
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Name:'
		self.fields['email'].label = 'E-mail:'
		self.fields['url'].label = 'Website:'
		self.fields['comment'].label = 'Comment:'
		
	def get_comment_model(self):
		return MarkdownComment
	
	def get_comment_create_data(self):
		data = super(MarkdownCommentForm, self).get_comment_create_data()
		data['is_markdown'] = self.cleaned_data['is_markdown']
		return data