from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home",
        "content": "Main page of the shop",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "bool": True
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")

