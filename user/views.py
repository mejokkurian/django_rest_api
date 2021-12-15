from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from user import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime


# Create your views here.

# api view
@api_view(['GET', 'POST'])
def login(request):
    user = User.objects.all()
    serializers = TaskSerializers(user,many = True)
    return Response(serializers.data)


# user registeration
@api_view(['POST'])
def register(request):
    serializers = TaskSerializers(data = request.data)
    serializers.is_valid(raise_exception = True)
    serializers.save()
    return Response(serializers.data)
  
    
# login page and user authentication checking and jwt token genaration
@api_view(['POST'])
def login_sub(request):
    username = request.data["username"]  
    password = request.data["password"]  
    useerr = authenticate(username = username, password = password)
    print(useerr)
    if useerr is None:
        return Response(False)
    
    payload = { 
        'id' : useerr.id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat' : datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, 'secret',algorithm='HS256')
    responce = Response()
    responce.set_cookie(key = 'jwt', value = token, httponly = False, path = '/', )
    responce.data = {
        'jwt': token
    }
    return responce


# check user authentication using jwt tokens
@api_view(['GET'])
def user_view(request):
    # token = request.COOKIES.get('jwt')
    token = request.headers['Authorization']
    print(token,"dfgdfgdfgdf")
    if not token:
        return Response(False)        
    try:
        payload = jwt.decode(token,'secret', algorithms =['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Key expired")
    
        
    user = User.objects.filter(id = payload['id']).first()
    serializers = TaskSerializers(user)
    return Response(serializers.data)


# user logout
@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        "message" : "logout successfully!!!!"
    }
    return response
    
    