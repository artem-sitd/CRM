from django.urls import path

from .views import (AdsUpdateView, DeleteAds, DetailAds, ListAds, ads_stat,
                    create_ads)

app_name = "ads"
urlpatterns = [
    path("create/", create_ads, name="ads-create"),
    path("<int:pk>/delete/", DeleteAds.as_view(), name="ads-delete"),
    path("detail/<int:pk>/", DetailAds.as_view(), name="ads-detail"),
    path("<int:pk>/edit/", AdsUpdateView.as_view(), name="ads-edit"),
    path("list/", ListAds.as_view(), name="ads-list"),
    path("statistic/", ads_stat, name="ads-statistic"),
]
