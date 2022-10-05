from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import index, login_facebook, login_process

urlpatterns = [
	path('', index ),
	path('/login/facebook', login_facebook ),
	path('/login/login_process', login_process ),

]


