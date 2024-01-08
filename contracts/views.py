from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from .models import Contract

from .forms import ContractsForm


# Дописать permission
def contracts_create(request):
    success_url = reverse_lazy('ads:ads-list')
    if request.method == 'POST':
        form = ContractsForm(request.POST)
        if form.is_valid():
            form.save()
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
    pass


# Дописать permission
class ContractDelete(DeleteView):
    pass


# Дописать permission
class ContractUpdate(UpdateView):
    pass
