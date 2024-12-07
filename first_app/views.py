from lib2to3.fixes.fix_input import context

from django.shortcuts import render

def index(request):
    context1 = {
        "date": "07.12.2024"
    }
    return render(request, "index.html", context1)
def riddle(request):
    context2 = {}
    return render(request,"riddle.html", context2)
def answer(request):
    context3 = {}
    return render(request,"answer.html", context3)