from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadModelForm

# Create your views here.

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, id):
    context = {
        "lead": Lead.objects.get(id=id)
    }
    return render(request, "leads/lead_detail.html", context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads") 

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

def lead_update(request, id):
    lead = Lead.objects.get(id=id)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads") 
    context = {
        "lead": lead,
        "form": form
    }
    return render(request, "leads/lead_update.html", context)

def lead_delete(request, id):
    lead = Lead.objects.get(id=id)
    lead.delete()
    return redirect("/leads") 