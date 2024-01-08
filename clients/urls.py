from django.urls import path
from .views import create_leads, ListLead, DetailLead, DeleteLead, LeadUpdateView

urlpatterns = [
    path("create/", create_leads, name="leads-create"),
    path("delete/<int:pk>", DeleteLead.as_view(), name="leads-delete"),
    path("detail/<int:pk>", DetailLead.as_view(), name="leads-detail"),
    path("edit/<int:pk>", LeadUpdateView.as_view(), name="leads-edit"),
    path("list/", ListLead.as_view(), name="leads-list"),

]
