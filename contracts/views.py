from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from clients.models import Client
from crm_django.decorators import groups_required

from .forms import ContractsForm
from .models import Contract


@groups_required("Managers")
def contracts_create(request):
    success_url = reverse_lazy("contracts:contracts-list")
    if request.method == "POST":
        form = ContractsForm(request.POST, request.FILES)
        if form.is_valid():
            valid_form = form.save()
            target_client = (
                Client.objects.filter(id=valid_form.ads_history.client.id)
                .only("state")
                .first()
            )
            target_client.state = "Active"
            target_client.save()
            return HttpResponseRedirect(success_url)
    else:
        form = ContractsForm()
    return render(request, "contracts/contracts-create.html", {"form": form})


@method_decorator(groups_required("Managers", "Admins"), name="dispatch")
class ContractList(ListView):
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"
    queryset = Contract.objects.filter(archived=False).order_by("id")


@method_decorator(groups_required("Managers", "Admins"), name="dispatch")
class ContractDetail(DetailView):
    model = Contract
    context_object_name = "object"
    template_name = "contracts/contracts-detail.html"


@method_decorator(groups_required("Managers"), name="dispatch")
class ContractUpdate(UpdateView):
    model = Contract
    form_class = ContractsForm
    template_name = "contracts/contracts-edit.html"
    success_url = reverse_lazy("contracts:contracts-list")


@method_decorator(groups_required("Managers"), name="dispatch")
class ContractDelete(DeleteView):
    model = Contract
    success_url = reverse_lazy("contracts:contracts-list")
    template_name = "contracts/contracts-delete.html"

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)
