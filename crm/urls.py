from django.contrib import admin
from django.urls import path

from leads.views import lead_list, lead_detail, lead_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', lead_list),
    path('leads/create', lead_create),
    path('leads/<int:id>', lead_detail),
]
