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
from django.urls import path, include
#from rest_framework.authtoken.views import obtain_auth_token

from base_admin.admin import base_admin_interface

from rest_framework.routers import SimpleRouter

from client import views as views_client
from contract import views as views_contract
from event import views as views_event

router = SimpleRouter()

router.register('clients', views_client.ClientViewSet)
router.register('contracts', views_contract.ContractViewSet)
router.register('events', views_event.EventViewSet)

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crm-admin/', base_admin_interface.urls),
    path('api/', include((router.urls, app_name))),
    #path('auth-token/', obtain_auth_token),
    path('', include('user.urls')),

]
