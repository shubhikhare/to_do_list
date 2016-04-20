from django.shortcuts import render,render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from to_do.models import Todo_List
from django.db import IntegrityError
from .forms import TodoForm
# Create your views here.

def  home(request):
	return render(request, 'index.html')

def signup(request):
	'''Signup for user'''

	if request.method == 'POST':
		print "Entered the if Section"
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		try:
			print "Entered the try section"
			user=User.objects.create_user(username=username,email=email,password=password)
			user.save()
			return HttpResponseRedirect("/login")
		except:
			return render(request,"register.html")

	elif request.method=='GET':
		return render(request, "register.html")

def login(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			username=request.POST['username']
			password=request.POST['password']
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					print "loggedin"
					auth.login(request,user)
					return HttpResponseRedirect("/display")
			else:
				print "none"
				return HttpResponseRedirect("/register")

		elif request.method == "GET":
			return render(request,"login.html")
	else:
		return HttpResponseRedirect("/")

def display(request):
	if request.user.is_authenticated():
		todolist=Todo_List.objects.filter(user=request.user.id)
		return render(request, "display.html", {'todolist':todolist})
	else:
		return HttpResponseRedirect("/")

def addtask(request):
	if request.method=='POST':
		try:
			title=request.POST['title']
			description=request.POST['description']
			details=Todo_List.objects.create(title=title,description=description,user=request.user)
			details.save()
		except IntegrityError as e:
			return render_to_response("display.html")

		todolist=Todo_List.objects.filter(user=request.user)
		return render(request, "display.html", {'todolist':todolist})
	elif request.method=="GET":
		return render(request, "todo.html")

def edit(request):
	form=TodoForm()
	if request.method=='POST':
		try:
			title=request.POST['title']
			description=request.POST['description']
			Todo_List.objects.filter(pk=request.user).update(title=title,description=description)
			details.save()
		except IntegrityError as e:
			return render_to_response("display.html")
		todolist=Todo_List.objects.filter(user=request.user)
		return render(request, "display.html", {'todolist':todolist})
	elif request.method=="GET":
		if request.method=='POST':
			form=TodoForm(request.POST)
			if form.is_valid():
				form.save()
				form.cleaned_data
		return render(request, "edit.html", {'form':form})
		
def delete(request):
	u=request.user.id
	Todo_List.objects.filter(pk=u).delete()
	todolist=Todo_List.objects.filter(user=request.user)
	return render(request, "display.html", {'todolist':todolist})

def logout(request):
	return render(request, "index.html")