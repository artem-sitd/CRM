from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, DetailView, ListView, UpdateView

from clients.models import HistoryAds
from contracts.models import Contract
from crm_django.decorators import groups_required
from products.models import Product

from .forms import AdsForm
from .models import Ads


@groups_required("Marketers")
def create_ads(request):
    success_url = reverse_lazy("ads:ads-list")
    if request.method == "POST":
        form = AdsForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(
                success_url
            )  # Перенаправление на страницу успеха (нужно настроить
            # на выход странице со ссылками, но для этого надо разграничить доступы
    else:
        form = AdsForm()  # Создайте пустую форму, если это GET-запрос
    return render(request, "ads/ads-create.html", {"form": form})


@method_decorator(groups_required("Marketers", "Admins"), name="dispatch")
class ListAds(ListView):
    template_name = "ads/ads-list.html"
    context_object_name = "ads"
    queryset = Ads.objects.filter(archived=False).order_by("id")


@method_decorator(groups_required("Marketers", "Admins"), name="dispatch")
class DetailAds(DetailView):
    template_name = "ads/ads-detail.html"
    model = Ads
    context_object_name = "object"


@method_decorator(groups_required("Marketers"), name="dispatch")
class DeleteAds(DeleteView):
    model = Ads
    success_url = reverse_lazy("ads:ads-list")
    template_name = "ads/ads-delete.html"

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)


@method_decorator(groups_required("Marketers"), name="dispatch")
class AdsUpdateView(UpdateView):
    model = Ads
    fields = "__all__"
    template_name = "ads/ads-edit.html"
    success_url = reverse_lazy("ads:ads-list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["product"].queryset = Product.objects.filter(archived=False)
        return form


@groups_required("Operators", "Marketers", "Managers", "Admins")
def ads_stat(request):
    data = []
    if request.method == "GET":
        ads_qs = Ads.objects.all().only("id", "price", "title")
        for ad in ads_qs:
            leads_list = HistoryAds.objects.filter(ads=ad.id).values_list(
                "id", flat=True
            )
            contract_list_ads = Contract.objects.filter(
                ads_history__id__in=leads_list
            ).only("price")
            profit = int(sum(i.price for i in contract_list_ads))

            dic_ad = {
                "pk": ad.pk,
                "title": ad.title,
                "client_potential": leads_list.count(),
                "client_active": contract_list_ads.count(),
                "profit": profit,
                "ad_price": int(ad.price),
                "ROI": round((profit / ad.price) * 100, 2),
            }
            data.append(dic_ad)
    return render(
        request,
        "ads/ads-statistic.html",
        context={"data": sorted(data, key=lambda x: x["ROI"], reverse=True)},
    )
