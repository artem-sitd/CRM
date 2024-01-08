from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, DetailView
from .forms import ClientsForm
from .models import Client


# Дописать permission
def create_leads(request):
    success_url = reverse_lazy('clients:leads-list')
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url)  # Перенаправление на страницу успеха (нужно настроить
            # на выход к странице list, но для этого надо разграничить доступы
    else:
        form = ClientsForm()  # Создайте пустую форму, если это GET-запрос
    return render(request, 'leads/leads-create.html', {'form': form})


# Дописать permission
class ListLead(ListView):
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'
    queryset = Client.objects.filter(state='POTENTIAL').order_by('id')


# Дописать permission
class DetailLead(DetailView):
    template_name = 'leads/leads-detail.html'
    model = Client
    context_object_name = 'object'

    def get_queryset(self):
        qs = get_object_or_404(Client, pk=self.kwargs['pk'])
        return qs


# Дописать permission
class DeleteLead(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:leads-list')
    template_name = 'leads/leads-delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.state = 'INACTIVE'  # не удаляем, а меняем его статус на inactive
        self.object.save()
        return HttpResponseRedirect(self.success_url)


# Дописать permission
class LeadUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('clients:leads-list')
