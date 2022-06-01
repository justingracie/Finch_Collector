from email.mime import image
from multiprocessing.sharedctypes import Value
from ssl import ALERT_DESCRIPTION_USER_CANCELLED
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Coin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView


class Home(TemplateView):
    template_name="home.html"

class About(TemplateView):
    template_name="about.html"


class CoinList(TemplateView):
    template_name = "coin_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coins'] = Coin.objects.all()
        return context

class CoinCreate(CreateView):
    model = Coin
    fields = ['type', 'year', 'img', 'value', 'quantity']
    template_name = 'coin_create.html'
    success_url = "/coins/"

class CoinDetail(DetailView):
    model = Coin
    template_name = "coin_detail.html"

class CoinUpdate(UpdateView):
    model = Coin
    fields = ['type', 'year', 'img', 'value', 'quantity']
    template_name = "coin_update.html"
    success_url = "/coins/"