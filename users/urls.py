from django.urls import path

from .views import Logout_view, generalStat, login_view

app_name = "users"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", Logout_view.as_view(), name="logout"),
    path("stat/", generalStat, name="stat"),
]
