from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import index, login, login_process

urlpatterns = [
	path('', index ),
	path('login', login ),
	path('login_process', login_process ),

]
