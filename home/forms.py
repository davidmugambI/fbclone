from django import forms
from . models import Post

# class HomeForm(forms.Form):
#     post = forms.CharField()

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'What is on your mind...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)