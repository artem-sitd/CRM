from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, DetailView
from .forms import ClientsForm, CheckPhoneForm
from .models import Client
from django.contrib import messages


# Дописать permission. Первичная проверка клиента
def leads_check(request):
    if request.method == 'POST':
        form = CheckPhoneForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone']

            # Проверяем существует ли клиент с таким номером телефона
            existing_client = Client.objects.filter(phone=phone_number).first()
            if existing_client is None:
                # Если клиент не существует, открываем окно для окончания редактирования клиента (предварительно создаем его)
                new_client = form.save()
                messages.success(request, 'Клиент в базе не обнаружен, создаем нового')
                return redirect(reverse_lazy('clients:leads-detail', kwargs={'pk': new_client.pk}))

            else:
                if existing_client.state == 'Active':
                    # Если клиент активен, показываем сообщение об успешном сообщении
                    messages.success(request, 'Клиент является активным - переходим к созданию контракта')
                    return redirect('contracts-create')  # Перенаправление на страницу создания контракта

                if existing_client.state == 'Potential':
                    messages.success(request, 'Клиент уже является потенциальным - переходим к созданию контракта')
                    return redirect('contracts-create')  # Перенаправление на страницу создания контракта

                else:
                    # Если клиент неактивен, показываем сообщение об успешном сообщении
                    messages.info(request, 'Клиент является неактивным - переходим к редактированию клиента')
                    # Перенаправление на страницу редактирования клиента
                    return redirect(reverse_lazy('clients:leads-detail', kwargs={'pk': existing_client.pk}))


    else:
        form = CheckPhoneForm()

    return render(request, 'leads/leads-check.html', {'form': form})


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


# Дописать permission
class DeleteLead(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:leads-list')
    template_name = 'leads/leads-delete.html'

    def form_valid(self, form):
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
