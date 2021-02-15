"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from adminapp import views

urlpatterns = [
    path('adminpage', views.adminpage, name='adminpage'),
    path('graph1', views.graph1, name='graph1'),
    path('graph2', views.graph2, name='graph2'),
    path('graph3', views.graph3, name='graph3'),
    path('graph4', views.graph4, name='graph4'),
]
