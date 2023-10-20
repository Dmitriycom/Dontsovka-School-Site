from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def students(request):
    return render(request, "main/students.html")

def parents(request):
    return render(request, "main/parents.html")

def teachers(request):
    return render(request, "main/teachers.html")

def educProc(request):
    return render(request, "main/educProc.html")

def educProc2(request):
    return render(request, "main/educProc2.html")

def news(request):
    return render(request, "main/news.html")

def mail(request):
    return render(request, "main/mail.html")