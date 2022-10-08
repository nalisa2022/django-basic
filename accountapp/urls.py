from django.urls import path
from .views import home, test

app_name='accountapp' # localhost:8000/account/helloworld = accountapp:hello_world

urlpatterns = [
	path('', home ),
	path('test', test),
]


