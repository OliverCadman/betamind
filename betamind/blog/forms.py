from django import forms
from django.core.exceptions import ValidationError
from .models import Mood, Post, Comment
import re


class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label="How are you doing?",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "I need a hand."
        })
    )

    content = forms.CharField(
        required=False,
        label="What's on your mind?",
        widget=forms.Textarea(attrs={
            'rows': 6,
            'width':'100%',
            'class': 'form-control',
            'placeholder': 'Please let us know.'}))
    
    mood = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-select"}),
        initial="Happy",
        queryset=Mood.objects.all(),
        label="Select Your Mood"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'mood']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'mood': 'Select your Mood'
        }
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
        }

    
    def clean_title(self):
        """
        Raise a validation error if additional_info
        field consists of only numbers.
        Uses regex pattern to compare against input's value.
        """
        title = self.cleaned_data["title"]
        regex = "^[0-9]+$"
        if re.match(regex, title):
            raise ValidationError(
                "Please enter words as well as numbers.")
        else:
            return title

    def clean_content(self):
        """
        Raise a validation error if additional_info
        field consists of only numbers.
        Uses regex pattern to compare against input's value.
        """
        content = self.cleaned_data["content"]
        regex = "^[0-9]+$"
        if re.match(regex, content):
            raise ValidationError(
                "Please enter words as well as numbers.")
        else:
            return content

