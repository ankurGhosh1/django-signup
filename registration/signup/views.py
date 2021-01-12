from django.shortcuts import render
from django.http import JsonResponse
import requests 
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

    if(password == password2 and len(password) > 8):
        user = User(username= username, first_name = firstname, last_name = lastname, email=email, password=password)
        user.set_password(password)
        user.save()
        return JsonResponse({'message': 'User Created Successfully'})
    else:
        return JsonResponse({'message': 'Password Do not Match'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return JsonResponse({'message': 'Logged In'})
        else:
            return JsonResponse({'message': 'Invalid Credentials'})


