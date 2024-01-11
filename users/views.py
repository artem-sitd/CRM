from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.db.models import Case, Count, When
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from ads.models import Ads
from clients.models import Client
from crm_django.decorators import groups_required
from products.models import Product

from .forms import LoginForm


def login_view(request):
    success_url = reverse_lazy("users:stat")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            user = authenticate(username=username, password=pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        success_url
                    )  # Перенаправление на страницу успеха (нужно настроить
                    # на выход к странице со ссылками, но для этого надо разграничить доступы
                else:
                    form.add_error("__all__", "Ошибка! учетная запись не активна")
            else:
                form.add_error("__all__", "ошибка, не верны логин или пароль!")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


class Logout_view(LogoutView):
    next_page = "/users/login/"


@groups_required("Operators", "Marketers", "Managers", "Admins")
def generalStat(request):
    print(request.user.get_all_permissions())
    if request.method == "GET":
        clients = Client.objects.aggregate(
            leads_count=Count(Case(When(state="POTENTIAL", then=1))),
            customers_count=Count(Case(When(state="Active", then=1))),
        )
        context = {
            "products_count": Product.objects.filter(archived=False).only("id").count(),
            "advertisements_count": Ads.objects.filter(archived=False)
            .only("id")
            .count(),
            "leads_count": clients["leads_count"],
            "customers_count": clients["customers_count"],
        }
        return render(request, "users/index.html", context=context)
    return HttpResponse("только метод get")
