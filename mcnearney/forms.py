from django import forms

class ContactForm(forms.Form):
	sender_name = forms.CharField(max_length=64, label='Name:')
	sender_email = forms.EmailField(label='Email:')
	subject = forms.CharField(max_length=64, label='Subject:')
	message = forms.CharField(widget=forms.Textarea, label='Message:')