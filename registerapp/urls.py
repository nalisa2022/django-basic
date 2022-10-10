from django.urls import path
from .views import register_patient

app_name='registerapp' # localhost:8000/account/helloworld = accountapp:hello_world

urlpatterns = [
	path('', register_patient, name='register' ),
]


