"""wallet_project URL Configuration

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

from wallet_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', registration_view, name="registrations" ),
    path('login', login_view, name="login" ),
    path('checkbalance', check_balance_view, name="checkbalance" ),
    path('transaction/request', transactions_request_view, name="newtransaction" ),
    path('transaction/conformation', transaction_update_view, name="transaction" ),
    # path('p2p', create_p_2_p_view, name="create_p2p" ),
]
