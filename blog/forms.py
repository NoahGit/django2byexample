# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/12/29 21:05
# File   : forms.py.py
# IDE    : PyCharm
from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')