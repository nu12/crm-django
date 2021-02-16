from django.urls import path

from .views import AgentListView, AgentCreateView

app_name="agents"

urlpatterns = [
    path('', AgentListView.as_view(), name='list'),
    path('create', AgentCreateView.as_view(), name='create'),
    #path('<int:pk>', LeadDetailView.as_view(), name='detail'),
    #path('<int:pk>/update', LeadUpdateView.as_view(), name='update'),
    #path('<int:pk>/delete', LeadDeleteView.as_view(), name='delete'),
]
