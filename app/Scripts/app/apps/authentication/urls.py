# -*- encoding: utf-8 -*-


from django.urls import path
from .views import login_view, register_user, add
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('addDetails/', views.add, name='add'),
    path('addDetails.html/', views.addDetails, name="addDetails")

]
