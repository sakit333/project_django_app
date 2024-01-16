from django.urls import path,include
from myApp import views

urlpatterns = [
    path('', views.signup),
    path('index/', views.index),
    # path('login/', views.login),
    # path('signup/', views.signup)
]