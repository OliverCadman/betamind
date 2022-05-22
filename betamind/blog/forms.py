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
    title = forms.CharField(
        label = 'Post Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
            }))

    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 6,
            'width':'100%',
            'class': 'form-control',
            'placeholder': 'Enter Image/YouTube Video Url or a text quote'}))

    class Meta:
        model = Post
        fields = ['title', 'slug', 'post_sender',  'mood', 'content']
        labels = {
            'title': 'Title',
            'post_sender': 'Author',
            'mood': 'Mood',
            'content': 'Content',
            'slug': 'Description',
        }
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['post_sender'].queryset = User.objects.filter(is_superuser=False)
            
            mood = Mood.objects.all()

# class EditPost(forms.ModelForm):
    title = forms.CharField(
        label = 'Post Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
            }))

    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 6,
            'width':'100%',
            'class': 'form-control',
            'placeholder': 'Edit your Betamind Post here!'}))

    class Meta:
        model = Post
        fields = ['title', 'slug', 'post_sender',  'mood', 'content']
        labels = {
            'title': 'Title',
            'post_sender': 'Author',
            'mood': 'Mood',
            'content': 'Content',
            'slug': 'Description',
        }
        # style the labels

        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),

        }