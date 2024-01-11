from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from .models import Contract
from clients.models import Client
from .forms import ContractsForm


# Дописать permission
def contracts_create(request):
    success_url = reverse_lazy('contracts:contracts-list')
    if request.method == 'POST':
        form = ContractsForm(request.POST)
        if form.is_valid():
            valid_form = form.save()
            target_client = Client.objects.filter(id=valid_form.ads_history.client.id).only('state').first()
            target_client.state = 'Active'
            target_client.save()
            return HttpResponseRedirect(success_url)
    else:
        form = ContractsForm()
    return render(request, 'contracts/contracts-create.html', {'form': form})


# Дописать permission
class ContractList(ListView):
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'
    queryset = Contract.objects.filter(archived=False).order_by('id')


# Дописать permission
class ContractDetail(DetailView):
    model = Contract
    context_object_name = 'object'
    template_name = 'contracts/contracts-detail.html'


# Дописать permission
class ContractUpdate(UpdateView):
    model = Contract
    form_class = ContractsForm
    template_name = 'contracts/contracts-edit.html'
    success_url = reverse_lazy('contracts:contracts-list')


# Дописать permission
class ContractDelete(DeleteView):
    model = Contract
    success_url = reverse_lazy('contracts:contracts-list')
    template_name = 'contracts/contracts-delete.html'

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)
