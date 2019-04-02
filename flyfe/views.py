from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

import random

from .models import *


def cards_list(request):
    cards = Card.objects.all()
    return render(request, 'flyfe/index.html', context={'cards': cards})

class CardDetail(View):
    def get(self, request, slug):
        card = get_object_or_404(Card, slug__iexact=slug)
        return render(request, 'flyfe/card_detail.html', context={'card': card})

def start_page(request):
    return render(request, 'flyfe/start_page.html')

def random_card(request):
    cards = list(Card.objects.all())
    card = random.choice(cards)
    return render(request, 'flyfe/card_detail.html', context={'card': card})
