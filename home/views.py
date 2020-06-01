from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def profile(request):
    return render(request, 'home/profile.html')

def profile_edit(request):
    return render(request, 'home/profile_edit.html')
