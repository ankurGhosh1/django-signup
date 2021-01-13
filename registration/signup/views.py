from django.shortcuts import render
from django.http import JsonResponse
import requests 
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from . models import UserExtended
import json
# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

    if(password == password2 and len(password) > 8):
        user = User(username= username, first_name = firstname, last_name = lastname, email=email, password=password)
        user.set_password(password)
        user.save()
        userExtended = UserExtended(
            user = User.objects.get(username = username),
            phone = phone
        )
        userExtended.save()
        return JsonResponse({'message': 'User Created Successfully'})
    else:
        return JsonResponse({'message': 'Password Do not Match or Password is less than 8 characters'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        user_id = User.objects.get(username = username)

        user_phone = UserExtended.objects.filter(user_id=user_id).values('phone')
        phone = list(user_phone)
        print(phone)

        if user is not None:
            auth.login(request, user)
            return JsonResponse({
                'username': user.username,
                'name': user.first_name,
                'lastname': user.last_name,
                'email': user.email,
                'phone': phone
            })
        else:
            return JsonResponse({'message': 'Invalid Credentials'})


