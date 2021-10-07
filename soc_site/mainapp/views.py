import json
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, DeleteView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator



def index(request):
    return render(request, 'mainapp/index.html', {})


def auth(request):
    form = UserCreationForm
    return render(request, "mainapp/auth.html", {})


class AuthView(CreateView):
    
    form_class = UserCreationForm
    template_name = "mainapp/auth.html"
    success_url = reverse_lazy("main_app:auth")


class JsonAuthView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return JsonResponse({"data": "hello"}, safe=False)