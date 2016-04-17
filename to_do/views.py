from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from to_do.models import Todo_List
from django.db import IntegrityError
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
		todolist=Todo_List.objects.filter(user=request.user)
		return render(request, "display.html", {'todolist':todolist})
	else:
		return ('/Please Login/', "index.html")

def addtask(request):
	return render(request, "todo.html")

def todo(request):
	try:
		details=Todo_List(title='title',description='description')
		details.save()
	except IntegrityError as e:
		return render_to_response("display.html")

def edit(request):
	details=Todo_List(title=title,description=description)
	details.objects
	Todo_List.objects.filter(pk=details.id).update(title='title',description='description')
	details.save()

def logout(request):
	return render(request, "index.html")