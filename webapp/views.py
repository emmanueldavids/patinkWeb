from django.shortcuts import render, redirect, get_object_or_404
# from .models import Task
# from .forms import TaskForm

def index(request):
    # tasks = Task.objects.all()
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def portfolio(request):
    return render(request, 'webapp/portfolio.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def services(request):
    return render(request, 'webapp/services.html')