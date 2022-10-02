from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "author": "Gaurav Singhal",
        "website": {
            "domain": "https://pluralsight.com",
            "views": 200
        },
        "odds": [1, 3, 5]
    }
    return render(request, "index.html", context)

def login(request):
	return render(request, "login.html")

