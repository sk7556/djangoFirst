from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'contents', 'main_image']

class LicatForm(forms.Form):
    tit = forms.CharField(max_length=20)
    con = forms.CharField()