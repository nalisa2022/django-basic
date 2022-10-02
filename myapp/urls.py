from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import index, login

urlpatterns = [
	path('', index ),
	path('login', login ),
]
