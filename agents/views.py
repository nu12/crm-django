from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm

from leads.models import Agent

# Create your views here.

class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"
    
    def get_queryset(self):
        request_user_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_organisation)

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        request_user_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_organisation)

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        request_user_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_organisation)

    def get_success_url(self):
        return reverse("agents:list")

class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html" # <- Template view
    
    def get_queryset(self):
        request_user_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_organisation)
    
    def get_success_url(self):
        return reverse("agents:list")