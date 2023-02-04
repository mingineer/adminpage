from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 어드민페이지 테스트
def hello_world(request):
    return HttpResponse('Admin Page Account Test')
