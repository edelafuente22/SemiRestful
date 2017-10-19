# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new.html')

def edit(request, id):
    context = {
        'user': User.objects.get(id = id) 
    }
    return render(request, 'users/edit.html', context)

def create(request):
    if request.method == 'POST':
        usr = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/users/'+str(usr.id))

def show(request, id):
    context = {
        'user': User.objects.get(id = id) 
    }
    # print context
    # for user in users:
    #     first_name = request.session['first_name']
    #     last_name = request.session['last_name']
    #     email = request.session['email']
    return render(request, 'users/show.html', context)
        
def delete(request, id):
    # if request.method == 'POST':
    user_delete = User.objects.get(id = id).delete()
    return redirect('/users')

def update(request, id):
    if request.method == 'POST':
        user_update = User.objects.get(id = id)
        user_update.first_name = request.POST['first_name']
        user_update.last_name = request.POST['last_name']
        user_update.email = request.POST['email']
        user_update.save()
        return redirect('/users')