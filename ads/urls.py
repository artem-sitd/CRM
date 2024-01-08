from django.urls import path
from .views import create_ads, ListAds, DetailAds, DeleteAds, AdsUpdateView

urlpatterns = [
    path("create/", create_ads, name="ads-create"),
    path("delete/<int:pk>/", DeleteAds.as_view(), name="ads-delete"),
    path("detail/<int:pk>/", DetailAds.as_view(), name="ads-detail"),
    path("edit/<int:pk>/", AdsUpdateView.as_view(), name="ads-edit"),
    path("list/", ListAds.as_view(), name="ads-list"),
    # path("statistic/", ProfileApiView.as_view(), name="ads-statistic"),
]
