from django.urls import path
from .views import hello_world

app_name='accountapp' # localhost:8000/account/helloworld = accountapp:hello_world

urlpatterns = [
	path('/helloworld', hello_world, name='hello_world'),
	# path('login/facebook', login_facebook ),
	# path('login_process', login_process ),
]

