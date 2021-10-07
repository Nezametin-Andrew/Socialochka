from django.urls import path, re_path
from . import views


app_name = "main_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('auth/', views.AuthView.as_view(), name="auth"),
    path('auth/option', views.JsonAuthView.as_view(), name="json"),
]