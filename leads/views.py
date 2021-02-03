from django.shortcuts import render

# Create your views here.

def home_page(request):
    context = {
        "name": "Joe",
        "age": 35
    }
    return render(request, "leads/home_page.html", context)
