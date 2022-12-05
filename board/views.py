from django.shortcuts import render

from django.db.models import Q
from board.models import Corona
from datetime import datetime, timedelta

def list(request):
    posts = Corona.objects.all()
    q = datetime.now().date() - timedelta(1)
    print(q)
    if q:
        posts = posts.filter(stdday__icontains=f"{q}")
        print(type(posts))
        print(posts)
        return render(request, 'board/index.html', {'posts': posts, 'q': q})

    else:
        return render(request, 'board/index.html')

def read(request):
    posts = Corona.objects.values()
    q = datetime.now().date() - timedelta(1)
    print(q)
    if q:
        posts = posts.filter(stdday__icontains=f"{q}")
        print(type(posts))
        print(posts)
        return render(request, 'board/list.html', {'posts': posts, 'q': q})

    else:
        return render(request, 'board/list.html')

