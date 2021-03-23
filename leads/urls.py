from django.urls import path

from .views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView
from .views import CategoryListView, CategoryDetailView

app_name="leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='list'),
    path('create', LeadCreateView.as_view(), name='create'),
    path('<int:pk>', LeadDetailView.as_view(), name='detail'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='delete'),
    path('<int:pk>/assign', AssignAgentView.as_view(), name='assign'),

    path('categories', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
]
