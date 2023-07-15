from django.http import HttpResponse
from djangogirls.models import Post, User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from djangogirls.forms import PostForm, RegisterForm, LoginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'djangogirls/post_list.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'djangogirls/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form =  PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'djangogirls/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
        return render(request, 'djangogirls/post_edit.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Form valid')
    else:
        form = RegisterForm()
    return render(request, 'djangogirls/register.html', {'form':form})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password1'])
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            print('user',user)
            if user is not None:
                login(request, user)
        return render(request, 'djangogirls/login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'djangogirls/login.html', {'form':form})
