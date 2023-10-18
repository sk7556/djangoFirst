from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def tube(request):
    db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'tube/postlist.html', context)

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'tube/post.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) # 수정
        if form.is_valid():
            post = form.save()
            return redirect('post')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/create.html', {'form': form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post')
    return render(request, 'post/delete.html', {'post': post})

def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'tube/postlist.html', {'posts':posts})

signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',    
)

logout = LogoutView.as_view(
    next_page = settings.LOGOUT_URL,
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def logincheck(request):
    print(request.user.is_authenticated)
    print(request.user)
    return render(request, 'accounts/logincheck.html')

def loginfbv(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("login 성공")
        else:
            return HttpResponse("login 실패")
    return render(request, 'accounts/loginfbv.html')