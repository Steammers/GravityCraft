from django.contrib import admin
from django.urls import path
from minimum_prices.views import *

urlpatterns = [
    path('server/<int:server_id>/minimum-prices/', minimum_prices_page, name='minimum_prices_page'),
]
