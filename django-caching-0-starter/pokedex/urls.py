from django.urls import path
from .views import home, all

urlpatterns = [
    path("", home, name="home"),
    path("all", all, name="all_pokemon"),
]
