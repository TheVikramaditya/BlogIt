from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from . models import Blog

class CreateBlog(forms.ModelForm):
    title = forms.CharField(label="Title",error_messages={"required": "please fill it"},widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(label="Content",error_messages={"required": "please fill it"},widget=forms.Textarea(attrs={"rows":5,"class":"form-control"}))
    class Meta:
        model = Blog
        fields =['title','content']

    def save(self, commit=True, user=None, *args, **kwargs):
        instance = super(CreateBlog, self).save(commit=False, *args, **kwargs)
        instance.user = user
        if commit:
            instance.save()
        return instance