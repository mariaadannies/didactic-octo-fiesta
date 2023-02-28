from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404
from home.forms import PostsForm
from .models import Posts
import datetime
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_homepage(request):
    data_posts = Posts.objects.all()
    context = {
        'list_posts': data_posts,
        'is_authenticated': request.user.is_authenticated,
    }
    return render(request, "home.html", context)

@login_required(login_url='/home/login/')
def logged_in(request):
    data_posts = Posts.objects.all()
    context = {
        'list_posts': data_posts,
        'username': request.COOKIES['username'],
        'last_login': request.COOKIES['last_login'],
        'is_authenticated': request.user.is_authenticated,
    }
    return render(request, "home.html", context)

@login_required(login_url='/home/login/')
def profile(request):
    data_posts = Posts.objects.filter(user=request.user)
    context = {
        'list_posts': data_posts,
        'username': request.COOKIES['username'],
        'last_login': request.COOKIES['last_login'],
        'is_authenticated': request.user.is_authenticated,
    }
    return render(request, "profile.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('home:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(
                    reverse("home:logged_in"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                response.set_cookie('username', username)
                return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('home:show_homepage'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/home/login/')
def delete_posts(request, posts_id):
    if request.method == "POST":
        posts = get_object_or_404(Posts, pk=posts_id)
        posts.delete()

        return redirect(reverse('home:show_homepage'))

def show_json(request):
    posts = Posts.objects.all()
    data = serializers.serialize('json', posts)

    return HttpResponse(data, content_type='application/json')

@login_required(login_url='/home/login/')
def add_new_posts(request):
    if request.method == "POST":
        data = json.loads(request.POST['data'])

        new_posts = Posts(content=data["content"],  user=request.user)
        new_posts.save()

        return HttpResponse(serializers.serialize("json", [new_posts]), content_type="application/json")

    return HttpResponse()

@login_required(login_url='/home/login/')
@csrf_exempt
def delete_new_posts(request, id):
    if request.method == "POST":
        posts = get_object_or_404(Posts, pk=id, user=request.user)
        posts.delete()

    return HttpResponse()

@login_required(login_url='/home/login/')
@csrf_exempt
def edit_new_posts(request, id):
    queryset = Posts().objects.get(id=id)
    form = EditPosts(instance=queryset)
    if request.method == 'POST':
        form = EditPosts(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('home:logged_in')

    context = {
        'form':form
        }

    return render(request, 'edit.html', context)