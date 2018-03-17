from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import ProfileForm,UserForm,NewPostForm
from django.contrib.auth.models import User
from .models import Profile,Post

# Create your views here.
def index(request):
    post = Post.objects.filter(user_id=request.user.id)
    return render(request, "index.html",{"post":post})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

    else:
        form = NewPostForm()
    return render(request, 'post.html', {"form": form},)

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
