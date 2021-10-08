from django.urls import path, re_path
from . import views


app_name = "main_app"

urlpatterns = [
    path('', views.MainPageView.as_view(), name="index"),
    path('registration/', views.RegistrationView.as_view(), name="new_user"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('auth/option', views.JsonAuthView.as_view(), name="json"),
]