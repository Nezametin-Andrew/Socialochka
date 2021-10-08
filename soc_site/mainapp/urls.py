from django.urls import path, re_path
from . import views


app_name = "main_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.RegistrationView.as_view(), name="new_user"),
    path('auth/option', views.JsonAuthView.as_view(), name="json"),
    #path('check-auth', views.CheckAuthView.as_view(), name='check_auth'),
]