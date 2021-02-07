from django.urls import path

from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name="leads"

urlpatterns = [
    path('', lead_list, name='list'),
    path('create', lead_create, name='create'),
    path('<int:id>', lead_detail, name='detail'),
    path('<int:id>/update', lead_update, name='update'),
    path('<int:id>/delete', lead_delete, name='delete'),
]
