from crm_django.decorators import groups_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from .forms import CheckPhoneForm, LeadUpdateForm
from .models import Client, HistoryAds


# Первичная проверка клиента
@groups_required("Operators")
def create_leads(request):
    if request.method == "POST":
        form = CheckPhoneForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone"]

            # Проверяем существует ли клиент с таким номером телефона
            existing_client = Client.objects.filter(phone=phone_number).first()
            if existing_client is None:
                # Если клиент не существует, открываем окно для окончания редактирования клиента (предварительно создаем его)
                new_client = form.save()
                messages.success(request, "Клиент в базе не обнаружен, создаем нового")
                return redirect(
                    reverse_lazy("clients:leads-detail", kwargs={"pk": new_client.pk})
                )

            else:
                if existing_client.state == "Active":
                    # Если клиент активен, показываем сообщение об успешном сообщении
                    messages.success(
                        request,
                        "Клиент является активным - переходим к созданию контракта",
                    )
                    return redirect(
                        reverse_lazy("contracts:contracts-create")
                    )  # Перенаправление на страницу создания контракта

                if existing_client.state == "Potential":
                    messages.success(
                        request,
                        "Клиент уже является потенциальным - переходим к созданию контракта",
                    )
                    return redirect(
                        reverse_lazy("contracts:contracts-create")
                    )  # Перенаправление на страницу создания контракта

                else:
                    # Если клиент неактивен, показываем сообщение об успешном сообщении
                    messages.info(
                        request,
                        "Клиент является неактивным - переходим к редактированию клиента",
                    )
                    # Перенаправление на страницу редактирования клиента
                    return redirect(
                        reverse_lazy(
                            "clients:leads-detail", kwargs={"pk": existing_client.pk}
                        )
                    )

    else:
        form = CheckPhoneForm()

    return render(request, "leads/leads-create.html", {"form": form})


@method_decorator(groups_required("Managers", "Operators", "Admins"), name="dispatch")
class ListLead(ListView):
    template_name = "leads/leads-list.html"
    context_object_name = "leads"
    queryset = Client.objects.filter(state="POTENTIAL").order_by("id")


@method_decorator(groups_required("Managers", "Operators", "Admins"), name="dispatch")
class ListInactive(ListView):
    template_name = "leads/leads-inactive.html"
    context_object_name = "leads"
    queryset = Client.objects.filter(state="INACTIVE").order_by("id")


@method_decorator(groups_required("Operators", "Admins"), name="dispatch")
class DetailLead(DetailView):
    template_name = "leads/leads-detail.html"
    model = Client
    context_object_name = "object"


@method_decorator(groups_required("Operators"), name="dispatch")
class DeleteLead(DeleteView):
    model = Client
    success_url = reverse_lazy("clients:leads-list")
    template_name = "leads/leads-delete.html"

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.state = "INACTIVE"  # не удаляем, а меняем его статус на inactive
        self.object.save()
        return HttpResponseRedirect(self.success_url)


@method_decorator(groups_required("Operators"), name="dispatch")
class LeadUpdateView(UpdateView):
    model = Client
    form_class = LeadUpdateForm
    template_name = "leads/leads-edit.html"
    success_url = reverse_lazy("clients:leads-list")

    def form_valid(self, form):
        # Получаем объект Client
        client = form.save()
        if not HistoryAds.objects.filter(ads=client.ads, client=client).exists():
            # Здесь создайте объект HistoryAds на основе данных из объекта Client, если такой записи нет
            HistoryAds.objects.create(ads=client.ads, client=client)
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(groups_required("Managers", "Operators", "Admins"), name="dispatch")
class ActiveClient(ListView):
    template_name = "leads/leads-active.html"
    context_object_name = "leads"
    queryset = Client.objects.filter(state="Active").order_by("id")
