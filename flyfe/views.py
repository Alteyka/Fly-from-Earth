from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import View
from .forms import NewPlanetForm, LoginForm
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
import random
from .models import *
from django import forms


class CardCreate(LoginRequiredMixin, View):

    def get(self, request):
        form = NewPlanetForm()
        return render(request, 'flyfe/card_create.html', context={'form': form})

    def post(self, request):
        bound_form = NewPlanetForm(request.POST)

        if bound_form.is_valid():
            created_planet = bound_form.save()
            return redirect(created_planet)

        return render(request, 'flyfe/card_create.html', context={'form': bound_form})

        raise_exception = True

def cards_list(request):
    cards = Card.objects.all()
    return render(request, 'flyfe/index.html', context={'cards': cards})


class CardDetail(View):
    def get(self, request, slug):
        card = get_object_or_404(Card, slug__iexact=slug)
        return render(request, 'flyfe/card_detail.html', context={'card': card, 'detail': True})


def start_page(request):
    return render(request, 'flyfe/start_page.html')


# Mechanism of random generate cards.
def random_card(request):
    cards = list(Card.objects.all())
    card = random.choice(cards)
    return render(request, 'flyfe/card_detail.html', context={'card': card})



class CardUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):

    model = Card
    model_form = NewPlanetForm
    template = 'flyfe/card_update_form.html'
    raise_exception = True


class CardDelete(LoginRequiredMixin, View):

    def get(self, request, slug):
        card = Card.objects.get(slug__iexact=slug)
        return render(request, 'flyfe/card_delete_form.html', context={'card': card})

    def post(self, request, slug):
        card = Card.objects.get(slug__iexact=slug)
        card.delete()
        return redirect(reverse('cards_list_url'))
    raise_exception = True


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    error = ''
    form = LoginForm
    if user is not None:

        if user.is_active:
            login(request, user)
            return redirect('start_page_url')
        else:
            error = 'Login and password is incorrect'


    return render(request, 'flyfe/login.html', {'form': form, 'error': error})
