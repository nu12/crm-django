from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "leads/home_page.html")
