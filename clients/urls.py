from django.urls import path

from .views import (
    ActiveClient,
    DeleteLead,
    DetailLead,
    LeadUpdateView,
    ListInactive,
    ListLead,
    create_leads,
)

app_name = "clients"
urlpatterns = [
    path("create/", create_leads, name="leads-create"),
    path("delete/<int:pk>/", DeleteLead.as_view(), name="leads-delete"),
    path("detail/<int:pk>/", DetailLead.as_view(), name="leads-detail"),
    path("edit/<int:pk>/", LeadUpdateView.as_view(), name="leads-edit"),
    path("list/", ListLead.as_view(), name="leads-list"),
    path("list/active/", ActiveClient.as_view(), name="leads-active"),
    path("list/inactive/", ListInactive.as_view(), name="leads-inactive"),
]
