from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import ProfileForm,UserForm,PostForm
from django.contrib.auth.models import User
from .models import Profile,Post

# Create your views here.
def index(request):
    post = Post.objects.filter(user_id=request.user.id)
    return render(request, "index.html",{"post":post})

@transaction.atomic
def post(request, post_id):
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=request.user)
        if post_form.is_valid():
            post_form.save()
            return redirect('/')
    else:
        post_form = PostForm(instance=request.user)
    return render(request, 'post.html', {
        'post_form': post_form
    })

def profile(request, user_id):
    profile = Profile.objects.filter(user_id=request.user.id)
    return render(request, "profile.html", {"profile":profile})

@login_required
@transaction.atomic
def update_profile(request, user_id):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
