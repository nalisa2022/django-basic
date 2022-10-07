from django.urls import path
from .views import hello_world, home

app_name='accountapp' # localhost:8000/account/helloworld = accountapp:hello_world

urlpatterns = [
	# path('/helloworld', hello_world, name='hello_world'),
	path('', home ),
]


