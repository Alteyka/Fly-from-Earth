from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import *


def cards_list(request):
    cards = Card.objects.all()
    return render(request, 'flyfe/index.html', context={'cards': cards})

class CardDetail(View):
    def get(self, request, slug):
        card = get_object_404(Card, slug__iexact=slug)
        return render(request, 'flyfe/card_detail.html', context={'card': card})
