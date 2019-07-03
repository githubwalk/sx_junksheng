"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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


from app01 import views as app01_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', app01_v.gotoIndex),
    path('app01/login', app01_v.Homework01Login),
    path('app01/register', app01_v.Homework01Register),
    path('app01/ge', app01_v.getData),
    path('app01/sum/<int:num1>/<int:num2>', app01_v.sum),
    path('app01/hello', app01_v.hello),
    path('app01/gotoindex', app01_v.gotoindex),
]
