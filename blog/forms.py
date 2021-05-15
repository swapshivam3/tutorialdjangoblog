from django import forms
from django.db.models import fields
from .models import Comment, Upload_XL

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment        #meta configures the model
        fields = ('text',)


class Upload_XLForm(forms.ModelForm):
    class Meta:
        model=Upload_XL
        fields=('file_name',)
