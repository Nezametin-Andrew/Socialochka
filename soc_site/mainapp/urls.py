from django.urls import path
from . import views


app_name = "main_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('auth/', views.auth, name="auth"),
    path('json-req/', views.check_json, name="json"),
]