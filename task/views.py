from task.models import Task
from datetime import date
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

def home(request):

    msg=""
    if request.method == 'POST':
        task = request.POST['task']
        description = request.POST['description']
        today = date.today()
        
        # Check if email already exists
        if Task.objects.filter(task=task).exists():
            msg="task already exists!"           
            return render(request, 'task/home.html',{'status':msg})
        
        # Create a new user
        user = Task(task=task, description=description, date=today)        
        user.save()
        msg="Your account has been created successfully!"  
    
    return render(request, 'task/home.html',{'status':msg})


def task_list(request): 
    status = request.GET.get('status','all')   
    # task_list = Task.objects.order_by('date')
    # paginator = Paginator(task_list, 2)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.get_page(page_number)
    # context = {
    #     'tasks': page_obj,
    # }

    if status=='complete':
        task_list = Task.objects.order_by('date').filter(status='complete')
        print(status)        
    elif status=='pending' :
        task_list = Task.objects.filter(status='pending').order_by('date')
    else:
        task_list = Task.objects.all()

    paginator = Paginator(task_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'tasks': page_obj    }    
    return render(request, 'task/task_list.html',context)


def edit(request,id):  
    msg=""  
    task1=Task.objects.get(id=id)
    if request.method == 'POST':
        task = request.POST['task']
        description = request.POST['description']        
        today = date.today() 
        status = request.POST['status']    
             
        task1=Task.objects.get(id=id)
        # Create a new user
        task1.task=task        
        task1.description=description
        task1.completion_date=today
        task1.status=status     
        task1.save()
        msg="Your task has been updated successfully!"  

    return render(request, 'task/edit.html',{'status':msg,'task':task1})

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    msg="task deleted successfully"
    tasks1=Task.objects.filter(status="pending")
    return render(request, 'task/task_list.html',{'tasks':tasks1})