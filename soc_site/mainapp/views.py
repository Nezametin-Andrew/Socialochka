from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'mainapp/index.html', {})


def auth(request):
    return render(request, "mainapp/auth.html", {})


def check_json(request):
    return JsonResponse({"data": "hello"}, safe=False)