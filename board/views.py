from django.shortcuts import render

from django.db.models import Q
from board.models import Test4
from datetime import datetime, timedelta

def list(request):
    posts = Test4.objects.all()

    return render(request, 'board/list.html', {'posts': posts})

def read(request):
    posts = Test4.objects.all().order_by('-id')
    q = datetime.now().date() - timedelta(1)
    print("111111111111111")
    print(q)
    if q:
        posts = posts.filter(stdday__icontains=f"{q}")
        return render(request, 'board/list.html', {'posts': posts, 'q': q})

    else:
        return render(request, 'board/list.html')

