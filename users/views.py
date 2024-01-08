from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from .forms import LoginForm


def login_view(request):
    # success_url = reverse_lazy('users:statistic')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=username, password=pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/success/')  # Перенаправление на страницу успеха (нужно настроить
                    # на выход к странице со ссылками, но для этого надо разграничить доступы
                else:
                    form.add_error('__all__', 'Ошибка! учетная запись не активна')
            else:
                form.add_error('__all__', 'ошибка, не верны логин или пароль!')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


class Statistic(ListView):
    pass
