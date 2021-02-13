from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadModelForm

# Class based views

# TemplateView: basic class based view class
class LandingPageView(TemplateView):
    template_name = "landing.html"

# CRUD
class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all() # Default context: object_list
    # context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:list")

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:list")

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html" # <- Template view
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:list")
