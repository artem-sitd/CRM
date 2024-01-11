from django.urls import path
from .views import login_view, Logout_view, generalStat

app_name = 'users'
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", Logout_view.as_view(), name="logout"),
    path("stat/", generalStat, name="stat"),

]
