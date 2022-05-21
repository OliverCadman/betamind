from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.forms.models import modelformset_factory
from .models import Mood, Post, Comment
from .forms import PostForm
from profiles.models import UserProfile
from django.contrib.auth import get_user_model


# @login_required
# def select_mood(request):
#     """
#     Select mood to create a post
#     """
#     mood_form = MoodForm()
#     return render(request, 'blog/select_mood.html', {'mood_form': mood_form})


@login_required
def blog(request):
    """
    Render blog index page, and handle POST requests to
    add a blog to the page.
    """

    current_user = get_user_model().objects.get(username=request.user)

    if request.method == "POST":
        post_form = PostForm(request.POST or None)
        if post_form.is_valid():
            form = post_form.save(commit=False)
            form.post_sender = current_user
            form.save()
            return redirect(reverse("blog"))

    posts = Post.objects.all()
    moods = Mood.objects.all()

    post_form = PostForm()

    context = {
        'posts': posts,
        'moods': moods,
        'post_form': post_form
    }

    return render(request, 'blog.html', context)


# @login_required
# def edit_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     return render(request, 'blog/edit_post.html', {
#         'form': PostForm(instance=post),
#         'moods': Mood.objects.all(),
#         'post': post,
#     })


# @login_required
# def delete_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.delete()
#     return redirect('blog_index')
