from django.core.mail import send_mail
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

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created", 
            message="Goto the site to see the new lead", 
            from_email="test@test.com", 
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

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
