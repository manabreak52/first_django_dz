from lib2to3.fixes.fix_input import context

from django.shortcuts import render

def index(request):
    context1 = {
        "date": "07.12.2024"
    }
    return render(request, "index.html", context1)