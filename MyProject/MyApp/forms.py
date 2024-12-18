from .models import ImageModel
from django import forms
from .models import DocumentModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['name', 'image']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentModel
        fields = ['title', 'file']
