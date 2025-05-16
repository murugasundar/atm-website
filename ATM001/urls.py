"""
URL configuration for ATM001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.as_view(),name='home'),
    path('bank',bank.as_view(),name='bank'),
    path('dep',dep.as_view(),name='dep'),
    path('deposit',deposit.as_view(),name='deposit'),
    path('wdr',wdr.as_view(),name='wdr'),
    path('withdrawal',withdrawal.as_view(),name='withdrawal'),
    path('balance',balance.as_view(),name='balance'),
    path('change_pin',change_pin.as_view(),name='change_pin'),
    path('new_pin',new_pin.as_view(),name='new_pin'),
    path('home',home.as_view(),name='home'),


]
