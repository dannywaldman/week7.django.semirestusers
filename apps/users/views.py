from django.shortcuts import render, redirect, HttpResponse
from django import forms
from django.core.urlresolvers import reverse
from .forms import UserForm
from .models import User

def index(request):
    context = {'users': User.objects.all()}
    return render(request, 'users/index.html', context)

def add(request):
    if request.method == 'GET':
        return render(request, 'users/new.html', {'form': UserForm()})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
      
    return render(request, 'users/new.html', {'form': form})        
    
    
def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        if not form:
            form = UserForm()
    
    return render(request, 'users/new.html', {'form': form})

def show(request, id): 
    context = {'user': User.objects.get(id=id)}
    return render(request, 'users/show.html', context)

def edit(request, id):
    instance = User.objects.get(id=id)
    form = UserForm(instance=instance)
    return render(request, 'users/edit.html', {'form':form, 'id':id})

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect(reverse('index'))   

def modify(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('index'))        

