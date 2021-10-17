from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from .serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Register

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# --------------------- Api Views DOCKER --------------


@api_view(['GET', 'POST'])
def home_api_view(request):
    if request.method == 'GET':
        snippets = Register.objects.all()
        serializer = RegisterSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        new_user = RegisterSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response(new_user.data)


@api_view(['GET', 'PUT', 'DELETE'])
def update_or_delete_api_view(request, pk):
    user = Register.objects.get(id=pk)
    serialized_user = RegisterSerializer(user, many=False)
    if request.method == 'GET':
        return Response(serialized_user.data)

    elif request.method == 'PUT':
        serialized_user = RegisterSerializer(user, data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"message": "User Deleted Successfully!"})

# --------------------- Template Views --------------


def index_view(request):
    return render(request, 'index.html')


def register_view(request):
    return render(request, 'register.html')


def update_or_delete_view(request):
    return render(request, 'update.html')


def admin_view(request):
    return render(request, 'admin.html')


def signup_view(request):
    return render(request, 'signup.html')


def login_view(request):
    return render(request, 'login.html')
