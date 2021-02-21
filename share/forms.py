from django import forms
from .models import Image, Friend, Post  ##　imageいれてる

class HelloForm(forms.Form):
    name = forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(label='Email', \
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='Gender', required=False, \
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age = forms.IntegerField(label='Age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateField(label='Birth', \
        widget=forms.DateInput(attrs={'class':'form-control'}))

class TweetForm(forms.Form):
    content = forms.CharField(max_length=400, \
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':2})) 

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'title']         