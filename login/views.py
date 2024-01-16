from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def render_login(request):
    if 'name' in request.session:
        return HttpResponseRedirect(reverse('admin_dashboard'))
    return render(request,"Login.html")
def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Not Allowed")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user_obj = authenticate(request,username = username, password = password)
    if user_obj is not None:
        request.session['name'] = 'anoop'
        login(request, user_obj)
        return HttpResponseRedirect(reverse('admin_dashboard'))
    else:
        messages.error(request,'username or password not correct')
        return HttpResponseRedirect('/')
    
def admin_dashboard(request):
    if 'name' in request.session:
        return render(request, 'admin_dash.html')
    return HttpResponseRedirect('/')

def perfom_logout(request):
    if 'name' in request.session:
        request.session.clear
    logout(request)
    return HttpResponseRedirect('/')

def prelogin(request):
    if 'name' in request.session:
        return HttpResponseRedirect(reverse('admin_dashboard'))
    return render(request, 'prelogin.html')
    