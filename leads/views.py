from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadForm

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
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_lead = Lead.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                age = form.cleaned_data['age'],
                agent = Agent.objects.first()
            )
            return redirect("/leads/{}".format(new_lead.id)) 

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)