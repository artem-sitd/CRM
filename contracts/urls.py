from django.urls import path
from .views import contracts_create, ContractList, ContractDetail, ContractDelete, ContractUpdate

app_name = 'contracts'
urlpatterns = [
    path("create/", contracts_create, name="contracts-create"),
    path("<int:pk>/detail/", ContractDetail.as_view(), name="contracts-detail"),
    path("<int:pk>/delete/", ContractDelete.as_view(), name="contracts-delete"),
    path("<int:pk>/edit/", ContractUpdate.as_view(), name="contracts-edit"),
    path("list/", ContractList.as_view(), name="contracts-list"),

]
