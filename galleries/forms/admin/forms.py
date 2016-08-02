from django import forms
from galleries.models import Photo


class PhotoForm(forms.ModelForm):
    

    class Meta:
        model = Photo
        exclude = ['file_small', 'file_thumbnail']
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 3, 'cols': 15})
        }
