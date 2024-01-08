from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .forms import AdsForm
from .models import Ads


# Дописать permission
def create_ads(request):
    success_url = reverse_lazy('ads:ads-list')
    if request.method == 'POST':
        form = AdsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url)  # Перенаправление на страницу успеха (нужно настроить
            # на выход странице со ссылками, но для этого надо разграничить доступы
    else:
        form = AdsForm()  # Создайте пустую форму, если это GET-запрос
    return render(request, 'ads/ads-create.html', {'form': form})


# Дописать permission
class ListAds(ListView):
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'
    queryset = Ads.objects.filter(archived=False).order_by('id')


# Дописать permission
class DetailAds(DetailView):
    template_name = 'ads/ads-detail.html'
    model = Ads
    context_object_name = 'object'

    def get_queryset(self):
        qs = get_object_or_404(Ads, pk=self.kwargs['pk'])
        return qs


# Дописать permission
class DeleteAds(DeleteView):
    model = Ads
    success_url = reverse_lazy('ads:ads-list')
    template_name = 'ads/ads-delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)


# Дописать permission
class AdsUpdateView(UpdateView):
    model = Ads
    fields = '__all__'
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:ads-list')
