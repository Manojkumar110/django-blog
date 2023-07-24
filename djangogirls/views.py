import csv
from django.http import HttpResponse
from djangogirls.models import Post, User, Tags, Comment, Category, Tags
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from djangogirls.forms import PostForm, RegisterForm, LoginForm, UserForm, CommentForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    tags = Tags.objects.all() 
    return render(request, 'djangogirls/post_list.html', {'posts':posts, 'tags':tags})

def post_new(request):
    # post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form =  PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.slug=post.title
            post.published_date = timezone.now()
            post.save()
            for tag in request.POST.getlist('tags'):
                posts = get_object_or_404(Post, slug=post.slug)
                posts.tags.add(tag)
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request, 'djangogirls/addnewpost.html', {'form': form})

    # --------------------------------------------------
    # if request.method == 'POST':
    #     form =  PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.slug=post.title
    #         post.published_date = timezone.now()
    #         post.save()
    #         for tag in request.POST.getlist('tags'):
    #             posts = get_object_or_404(Post, slug=post.slug)
    #             posts.tags.add(tag)
    #             # posts.tags.add(tag)
    #         return redirect('post_list')
    # else:
    #     form = PostForm()
    #     return render(request, 'djangogirls/post_edit.html', {'form': form})
    # --------------------------------------------------
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            for tag in request.POST.getlist('tags'):
                post.tags.add(tag)
                # post.tags.set(tag)
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
            user = authenticate(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'],
                )
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'djangogirls/register.html', {'form':form})
    else:
        return render(request, 'djangogirls/register.html', {'form':form})

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # if '@' in name:
            #     user = authenticate(
            #         email=form.cleaned_data['username'],
            #         password=form.cleaned_data['password1'],
            #     )
            # else:
            #     usr_obj = User.objects.get(username=name).username
            #     user = authenticate(
            #         username=User.objects.get(username=usr_obj),
            #         password=form.cleaned_data['password1'],
            #     )
            try:
                try:
                    user = authenticate(
                        username=User.objects.get(username=name),
                        password=form.cleaned_data['password1'],
                        )
                    print('try obj', user)
                except:
                    user = authenticate(
                        email=User.objects.get(email__exact=name),
                        password=form.cleaned_data['password1'],
                    )
                    print('except obj', user)
            except Exception as e:
                return render(request, 'djangogirls/login.html', {'form':form})
            if user is not None:
                login(request, user)
                return redirect('/')
            return render(request, 'djangogirls/login.html', {'form':form})
    else:
        return render(request, 'djangogirls/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')


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
    # user = request.user
    userid = request.GET.get('id',)
    print(userid)
    # print('user id', id)
    postauthor = User.objects.get(id=userid)
    # print(user)
    return render(request, 'djangogirls/authordetail.html', {'postauthor':postauthor})



def post_detail(request, slug):
    # get post object
    post = get_object_or_404(Post, slug=slug)
    # user = User.objects.filter(post=post)
    # print(user)
    # list of active parent comments
    comments = post.comments.filter(active=True, parent__isnull=True).order_by('-created')
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            
            # assign ship to the comment
            new_comment.post = post
            new_comment.save()
            return redirect(f'/post/{post.slug}')
    else:
        comment_form = CommentForm()
    return render(request,
                  'djangogirls/post_detail.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})


def postCategory(request):
    cat = Category.objects.all()
    context = {'category':cat}
    return render(request, 'djangogirls/post_cat.html', context)



def catDetail(request, pk):
    cat = Category.objects.get(pk=pk).id
    posts = Post.objects.filter(category=cat)
    print(posts)
    context = {
        'posts':posts,
    }
    return render(request, 'djangogirls/cat_detail.html', context)
    # pass