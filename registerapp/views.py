from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from registerapp.models import register_patientinfo_db

# Create your views here.
def register_patient(request):
    # return HttpResponse('Register page')
    if request.method=='POST':
        temp=request.POST.get('text')

        # modeling
        new_data=register_patientinfo_db()
        new_data.name=temp
        new_data.save()

        # return render(request, "registerapp/register.html", context={'new_data_output': datas}) # make new item by referesh <--below, redirect can solve this
        return HttpResponseRedirect(reverse('registerapp:register')) 
        # return HttpResponseRedirect("/register") 
    else:
        datas=register_patientinfo_db.objects.all()
        return render(request, "registerapp/register.html", context={'new_data_output': datas})