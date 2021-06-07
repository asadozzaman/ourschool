from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('my/', views.my, name="my"),
]