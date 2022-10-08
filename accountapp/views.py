from hashlib import new
from django.http import HttpResponse
from django.shortcuts import render
from .models import helloworld
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @csrf_exempt
def home(request):
    return render(request, "accountapp/hello.html")

def test(request):
    # return HttpResponse('Hello')

    if request.method=='POST':
        temp=request.POST.get('text')

        # modeling
        new_data=helloworld()
        new_data.text=temp
        new_data.save()

        return render(request, "accountapp/hello.html", context={'new_data_output': new_data})
    else:
        return render(request, "accountapp/hello.html", context={'text':'Get method !'})