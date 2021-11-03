from django import forms
from django.forms import ModelForm
from . import models


class ImageUploadForm(ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']


class BlogUploadForm(ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'content']

class BlogEditForm(ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Blog
        fields = ['title', 'content']

class BlogDeleteForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)