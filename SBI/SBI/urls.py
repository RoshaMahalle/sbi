"""SBI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from loan import views as v1
from saving import views as v2
from deposit import  views as v3
from credit import views as v4


urlpatterns = [
    path('admin/', admin.site.urls),
    path('loan/',v1.show_loan),
    path('showdata/',v1.show_data),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', v1.logout),
    path('signup/', v1.signup),
    path('saving/',v2.show_saving),
    path('',v2.index),
    path('deposit/',v3.show_deposit),
    path('credit/',v4.show_credit),


]
