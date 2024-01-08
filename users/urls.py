from django.urls import path
from .views import login_view, Statistic

urlpatterns = [
    path("login/", login_view, name="login"),
    # path("statistic/", Statistic.as_view(), name="statistic"),

]
