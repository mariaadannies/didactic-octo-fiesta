from django.urls import path
from .views import show_homepage, register, logout_user, login_user, show_json, add_new_posts, delete_new_posts, edit_new_posts, logged_in, profile

app_name = 'home'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('logged_in/', logged_in, name='logged_in'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('json/', show_json, name='show_json'),
    path('add/', add_new_posts, name='add_new_posts'),
    path('delete/<int:id>/', delete_new_posts, name='delete_new_posts'),
    path('edit/<int:id>/', edit_new_posts, name='edit_new_posts'),
    path('profile/', profile, name='profile'),

]