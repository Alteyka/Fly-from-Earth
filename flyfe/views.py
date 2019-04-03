from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .forms import NewPlanetForm

import random

from .models import *

class CardCreate(View):

    def get(self, request):
        form = NewPlanetForm()
        return render(request, 'flyfe/card_create.html', context={'form': form})

    def post(self, request):
        bound_form = NewPlanetForm(request.POST)

        if bound_form.is_valid():
            created_planet = bound_form.save()
            return redirect(created_planet)

        return render(request, 'flyfe/card_create.html', context={'form': bound_form})


def cards_list(request):
    cards = Card.objects.all()
    return render(request, 'flyfe/index.html', context={'cards': cards})


class CardDetail(View):
    def get(self, request, slug):
        card = get_object_or_404(Card, slug__iexact=slug)
        return render(request, 'flyfe/card_detail.html', context={'card': card})


def start_page(request):
    return render(request, 'flyfe/start_page.html')

# Mechanism of random generate cards.
def random_card(request):
    cards = list(Card.objects.all())
    card = random.choice(cards)
    return render(request, 'flyfe/card_detail.html', context={'card': card})
