from django.shortcuts import render
from django.http import HttpResponse
from .models import Test1

def list(request):
    print('1111111111111111')
    posts = Test1.objects.all()
    print('222222222222222222')
    return render(request, 'board/list.html', {'posts': posts})
