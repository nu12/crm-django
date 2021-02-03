from django.contrib import admin
from django.urls import path

from leads.views import lead_list, lead_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', lead_list),
    path('leads/<id>', lead_detail),
]
