import csv
from django.http import HttpResponse
from djangogirls.models import Post, User, Tags, Comment
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from djangogirls.forms import PostForm, RegisterForm, LoginForm, UserForm, CommentForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.

def post_list(request):
    # posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    posts = Post.objects.all().order_by('-published_date')
    tags = Tags.objects.all() 
    return render(request, 'djangogirls/post_list.html', {'posts':posts, 'tags':tags})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # comments = Comment.objects.filter(active=False)
    comments = post.comments.filter(active=False)
    print('comments manoj', comments)
    if request.method == 'POST':
        comment_form  = CommentForm(request.POST)
        if comment_form.is_valid():
            # Assign the current post to the comment
            new_comment = comment_form.save(commit=False)
            print('new_comment',new_comment)
            # Save the comment to the database
            new_comment.post = post
            new_comment.save()
            return render(request, 'djangogirls/post_detail.html', {'post': post, 'comment_form':comment_form, 'comments':comments})
    else:
        comment_form = CommentForm()
        return render(request, 'djangogirls/post_detail.html', {'post': post, 'comment_form':comment_form, 'comments':comments})


# ===================================================================
# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=False)
#     # comments = post.comments.filter(active=True)
#     for i in comments:
#         print(i.name)
#         print(i.body)
#     if request.method == 'POST':
#         comment_form  = CommentForm(request.POST)
#         if comment_form.is_valid():
#             # Assign the current post to the comment
#             new_comment = comment_form.save(commit=False)
#             print('new_comment',new_comment)
#             # Save the comment to the database
#             new_comment.post = post
#             new_comment.save()
#             return render(request, 'djangogirls/post_detail.html', {'post': post, 'comment_form':comment_form, 'comments':comments})
#     else:
#         comment_form = CommentForm()
#         return render(request, 'djangogirls/post_detail.html', {'post': post, 'comment_form':comment_form, 'comments':comments})
# ===================================================================



def post_new(request):
    if request.method == 'POST':
        form =  PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request, 'djangogirls/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            for tag in request.POST.getlist('tags'):
                # post.tags.add(tag)
                post.tags.set(tag)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
        return render(request, 'djangogirls/post_edit.html', {'form': form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    else:
        return render(request, 'djangogirls/register.html', {'form':form})

def login_page(request):
    form = LoginForm()
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
        # return render(request, 'djangogirls/login.html', {'form':form})
        return redirect('/')
    else:
        
        return render(request, 'djangogirls/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return render(request, 'djangogirls/post_list.html')


def profile_view(request):
    user = request.user
    return render(request, 'djangogirls/userdetail.html', {'user':user})


def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('userprofileview')
    else:
        form = UserForm(instance=request.user)
        return render(request, 'djangogirls/updateprofile.html', {'form':form})

def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['first_name', 'user_profile', 'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country'])
    for user in User.objects.all().values_list('first_name', 'user_profile', 'email', 'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country'):
        writer.writerow(user)
    
    response['Content-Disposotion'] = 'attachment; filename="user.csv"'
    return response


def author_detail(request):
    user = request.user
    return render(request, 'djangogirls/authordetail.html', {'user':user})