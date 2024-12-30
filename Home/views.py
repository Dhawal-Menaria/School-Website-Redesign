from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def NotFound404(request,exception):
    return render(request, '404.html',status=404)

def InternalError500(request):
    return render(request, '500.html',status=500)