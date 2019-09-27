from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from .forms import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import random
from .models import *
from django import forms


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


@login_required(login_url='/flyfe/login/')
def cards_list(request):
    cards = Card.objects.all()
    return render(request, 'flyfe/cards_list.html', context={'cards': cards})


class CardDetail(View):
    def get(self, request, slug):
        card = get_object_or_404(Card, slug__iexact=slug)
        return render(request, 'flyfe/card_detail.html', context={'card': card, 'detail': True})


def start_page(request):
    return render(request, 'flyfe/start_page.html')


# Mechanism of random generate cards.
@login_required(login_url='/flyfe/login/')
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
    user = authenticate(request, username=username, password=password)
    form = LoginForm
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'Password or username are incorrect! Try again.')
    return render(request, 'flyfe/login.html', context={'form': form})


@login_required(login_url='/flyfe/login/')
def logout_view(request):
    logout(request)
    return render(request, 'flyfe/logout.html')


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'flyfe/start_page.html')
    else:
        form = SignUpForm()
    return render(request, 'flyfe/register.html', {'form': form})


def password_reset(request):
    pass
