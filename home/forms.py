from dataclasses import fields
from django.forms import ModelForm
from .models import Posts

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content']

class EditPosts(ModelForm):
    class Meta:
        model = Posts
        fields = ['content']