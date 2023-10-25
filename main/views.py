from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.all()
    return render(request, "main/index.html",  {"news": news})

def about(request):
    return render(request, "main/about.html")

def students(request):
    return render(request, "main/students.html")

def parents(request):
    return render(request, "main/parents.html")

def teachers(request):
    return render(request, "main/teachers.html")

def educProc(request):
    try:
        page = int(request.GET.get("page", 0))
        number = int(request.GET.get("number", 0))
    except:
        page = 2
        number = 1
    return render(request, "main/educProc.html", {"page": page, "number": number})

def educProc2(request):
    return render(request, "main/educProc2.html")

def news(request, newId=1):
    try:
        id = int(newId)
        new = News.objects.get(pk=id)
    except:
        id = 1
        news = News.objects.get(pk=id)
    news = News.objects.exclude(pk=id)
    return render(request, "main/news.html", {"new": new, "news": news})

def mail(request):
    return render(request, "main/mail.html")