from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'task/home.html')


def task_list(request):
    return render(request, 'task/task_list.html')
