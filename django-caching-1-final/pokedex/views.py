from django.shortcuts import render
from .models import Pokemon
import time


def home(request):
    start = time.perf_counter()
    grass = list(Pokemon.objects.filter(type="grass")[:5])
    nature = list(Pokemon.objects.filter(type="normal")[:5])
    water = list(Pokemon.objects.filter(type="water")[:5])
    categories = [("Normal", nature), ("Grass", grass), ("Water", water)]
    return render(
        request,
        "home.html",
        context={
            "categories": categories,
            "response_time": f"{(time.perf_counter()-start):6f} seconds",
        },
    )

# from django.views.decorators.cache import cache_page

# @cache_page(60)
def all(request):
    start = time.perf_counter()

    all_pokemon = list(Pokemon.objects.all())
    return render(
        request,
        "all.html",{"all_pokemon": all_pokemon,"response_time": f"{(time.perf_counter()-start):6f} seconds"},
    )
