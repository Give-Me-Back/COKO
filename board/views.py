from django.shortcuts import render

from django.db.models import Q
from board.models import Test4
from datetime import datetime, timedelta
gubun = ['검역', '전북', '충북', '강원', '제주', '합계', '대구', '경북', '서울', '인천', '경남', '세종', '대전', '경기', '광주', '울산', '부산', '전남', '충남']

def list(request):
    posts = Test4.objects.all()

    return render(request, 'board/korea.html', {'posts': posts})

def read(request):
    posts = Test4.objects.values()
    q = datetime.now().date() - timedelta(1)
    print(q)
    if q:
        posts = posts.filter(stdday__icontains=f"{q}")
        print(type(posts))
        print(posts)
        return render(request, 'board/list.html', {'posts': posts, 'q': q})

    else:
        return render(request, 'board/list.html')

