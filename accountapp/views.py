from django.http import HttpResponse
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @csrf_exempt
def home(request):
    return render(request, "accountapp/hello.html")

def test(request):
    # return HttpResponse('Hello')

    if request.method=='POST':
        return render(request, "accountapp/hello.html", context={'text':'POST method !'})
    else:
        return render(request, "accountapp/hello.html", context={'text':'Get method !'})