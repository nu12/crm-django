from django.urls import path

from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name="agents"

urlpatterns = [
    path('', AgentListView.as_view(), name='list'),
    path('<int:pk>', AgentDetailView.as_view(), name='detail'),
    path('create', AgentCreateView.as_view(), name='create'),
    path('<int:pk>/update', AgentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', AgentDeleteView.as_view(), name='delete'),
]
