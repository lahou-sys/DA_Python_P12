"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from base_admin.admin import base_admin_interface

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crm-admin/', base_admin_interface.urls)
]


# from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token

# from epicevents.basic_admin.admin import basic_admin_site


# urlpatterns = [
#     path('auth-token/', obtain_auth_token),
#     path('api/', include('config.api_router')),
#     # path('django-admin/', admin.site.urls),
#     path('api-admin/', basic_admin_site.urls),
# ]
