import json
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, DeleteView, ListView, CreateView
from django.contrib.auth.views import LoginView 
from .forms import RegistrationUserForm, LoginUserForm
from django.utils.decorators import method_decorator



class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/index.html')


class RegistrationView(CreateView):    

    form_class = RegistrationUserForm
    template_name = 'mainapp/auth.html'
    success_url = reverse_lazy('main_app:index')


class LoginView(LoginView):
    
    form_class = LoginUserForm
    template_name = "mainapp/auth.html"
    success_url = reverse_lazy('main_app:index')


class JsonAuthView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return JsonResponse({"data": "hello"}, safe=False)