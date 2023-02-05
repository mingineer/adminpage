from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# test admin page
def hello_world(request):
    return render(request, 'accountapp/hello_world.html')
