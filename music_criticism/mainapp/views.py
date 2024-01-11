from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Release, Comment
from .forms import UserRegisterForm, UserLoginForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

def index(request):
    releases = Release.objects.all()
    objects_per_page = 5
    paginator = Paginator(releases, objects_per_page)
    page = request.GET.get('page')

    try:
        objects_for_page = paginator.page(page)
    except PageNotAnInteger:
        objects_for_page = paginator.page(1)
    except EmptyPage:
        objects_for_page = paginator.page(paginator.num_pages)

    columns = range(3)
    return render(request, 'mainapp/index.html', {'releases': releases, 'columns': columns, 'objects_for_page': objects_for_page})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'mainapp/login.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'SignIn is success!')
            return redirect('login')
        else:
            messages.error(request, 'SignIn is failed!')
    else:
        form = UserRegisterForm()
    return render(request, 'mainapp/signin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')


class ReleaseDetailView(DetailView):
    model = Release
    template_name = 'mainapp/release_detail.html'
    context_object_name = 'release'


def add_comment(request, release_id):
    release = get_object_or_404(Release, pk=release_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.release = release
            comment.user = request.user
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    return render(request, 'mainapp/add_comment.html', {'form': form})

def release_detail(request, release_id):
    release = get_object_or_404(Release, pk=release_id)
    comments = Comment.objects.filter(release=release)
    return render(request, 'mainapp/release_detail.html', {'release': release, 'comments': comments})
