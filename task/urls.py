from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
   
   path('', views.home, name = 'home'),
   path('list', views.task_list, name = 'task_list'),
   path('edit/<int:id>', views.edit, name = 'edit'),
   path('delete/<int:id>', views.delete, name = 'delete'),

]
