import json

from django.http import JsonResponse
from django.shortcuts import render

from django.db.models import Q
from board.models import Corona
from datetime import datetime, timedelta
from board.models import News

def list(request):
    posts = Corona.objects.all().order_by('-localocccnt')
    g_posts = Corona.objects.all().order_by('stdday')
    g_posts = g_posts.values()
    g_posts =g_posts.filter(gubun__icontains="합계")
    print("ggggggg", g_posts)
    q = datetime.now().date() - timedelta(1)
    print(posts)
    if q:
        posts = posts.filter(stdday__icontains=f"{q}")
        print(type(posts))
        return render(request, 'board/index.html', {'posts': posts, 'q': q, 'g_posts':g_posts })

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

# def News(request):
#     posts = News.objects.all()
#     return render(request, 'board/news.html', {'posts': posts})


def News_list(request):
    posts = News.objects.all()
    return render(request, 'board/news.html', {'posts': posts})

def regions(request):
    gubun=request.GET.get('gubun')
    print(gubun)
    context = {'gubun': gubun}
    return JsonResponse(context)

