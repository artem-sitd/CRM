from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .forms import ProductsForm
from .models import Product


# Дописать permission
def create_product(request):
    success_url = reverse_lazy('products:products-list')
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(success_url)  # Перенаправление на страницу успеха (нужно настроить
            # на выход к странице со ссылками, но для этого надо разграничить доступы
    else:
        form = ProductsForm()  # Создайте пустую форму, если это GET-запрос
    return render(request, 'products/products-create.html', {'form': form})


# Дописать permission
class ListProducts(ListView):
    template_name = 'products/products-list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(archived=False).order_by('id')


# Дописать permission
class DetailProduct(DetailView):
    template_name = 'products/products-detail.html'
    model = Product
    context_object_name = 'object'


# Дописать permission
class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products-list')
    template_name = 'products\products-delete.html'

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)


# Дописать permission
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products\products-edit.html'
    success_url = reverse_lazy('products:products-list')
