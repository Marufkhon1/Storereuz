from django import forms
from django.contrib.auth.models import User


class SendEmailForm(forms.Form):
    name = forms.CharField(max_length=255,label="Name", help_text="Please enter your name")
    email = forms.EmailField()
    title = forms.CharField(max_length=50, label="Title", help_text="Please enter your title")
    message = forms.CharField(max_length=255, label="Message", help_text="Please enter Message",
                                  widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}))