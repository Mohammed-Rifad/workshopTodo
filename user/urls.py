from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
   
   path('index', views.index, name = 'user'),
   path('', views.login, name = 'login'),
   path('signup', views.signup, name = 'signup'),
   path('home', views.home, name = 'home'),

]
