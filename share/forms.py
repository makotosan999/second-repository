from django import forms
from .models import Image, Friend, Post  ##　imageいれてる

class FriendForm(forms.ModelForm):             
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']


class HelloForm(forms.Form):                        #これ使ってない
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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['picture', 'title']         