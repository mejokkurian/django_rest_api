from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
from django.shortcuts import render

# Create your views here.

# admin login
@api_view(['GET', 'POST'])
def admin_login(request):
    print("ITS CAME")
    username = request.data['username']
    password = request.data['password']
    print(username)
    print(password)
    admin = authenticate(username=username, password=password)
    if admin is not None:
        if admin.is_superuser:
            print("admin is superuser")
            return Response({
                "messages" : "Admin authencticated!!"
            })
    else:
        return Response({
            "messages" : "Admin authenication failed!!"
        })


# user account activate
@api_view(['GET', 'POST'])
def user_activate(request,id):
    user2 = User.objects.get(id=id)
    user2.is_active = True
    print("saving")
    user2.save()
    return Response ({
        "messages" : "user activated"
    })
   
   
# user account deactivate  
@api_view(['GET', 'POST'])
def user_deactivate(request,id):
    user2 = User.objects.get(id=id)
    user2.is_active = False
    print("saving")
    user2.save()
    return Response ({
        "messages" : "user has been deactivated"
    })
   
  
    