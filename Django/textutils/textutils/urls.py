"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('remove_punctuation', views.remove_punctuation, name="remove_punctuation"),
    path('capitalize_first', views.capitalize_first, name="capitalize_first"),
    path('space_remover', views.space_remover, name="space_remover"),
    path('char_count', views.char_count, name="char_count")

]
