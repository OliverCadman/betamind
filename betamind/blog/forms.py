from django import forms
from .models import Mood, Post, Comment

# class MoodForm(forms.ModelForm):
#     class Meta:
#         model = Mood
#         fields = ['name', 'mood', 'slug']
#         labels = {
#             'name': 'Mood Name',
#             'mood': 'Mood',
#             'slug': 'Slug',
#         }
#         widgets = {
#             'mood': forms.Select(attrs={'class': 'form-control'}),
#         }

class PostForm(forms.ModelForm):
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows':2,
            'width':'100%',
            'class': 'form-control',
            'placeholder': 'Enter Image/YouTube Video Url or a text quote'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'mood', 'slug']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'mood': 'Mood',
            'slug': 'Slug',
        }
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
        }
