from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
import random
from .forms import *
from .utils import *
from .tokens import account_activation_token


def created_by(model, request):
    obj = model.objects.latest('pk')
    if obj.author is None:
        obj.author = request.user
    obj.save()


class CardCreate(View):

    def get(self, request):
        form = NewCardForm()
        return render(request, 'flyfe/card_create.html', context={'form': form})

    def post(self, request):
        bound_form = NewCardForm(request.POST)
        model = Card

        if bound_form.is_valid():
            created_card = bound_form.save()
            created_by(model, request)
            return redirect(created_card)

        return render(request, 'flyfe/card_create.html', context={'form': bound_form})


def cards_list(request):
    cards = Card.objects.filter(author=get_user(request))
    return render(request, 'flyfe/cards_list.html', context={'cards': cards})


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
    return render(request, 'flyfe/card_detail.html', context={'card': card, 'detail': True})


class CardUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Card
    model_form = NewCardForm
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


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('flyfe/account_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your account'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration.')
    else:
        form = SignUpForm()
    return render(request, 'flyfe/signup.html', {'form': form})


# This function will check token if it valid then user will active and login.
def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'flyfe/start_page.html')
    else:
        return HttpResponse('Activation link is invalid!')


def get_my_user(request):
    user = get_user(request)
    return render(request, 'Fly-from-Earth/base.html', context={'user': user})
