from email.mime import image
from multiprocessing.sharedctypes import Value
from ssl import ALERT_DESCRIPTION_USER_CANCELLED
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Coin

class Home(TemplateView):
    template_name="home.html"

class About(TemplateView):
    template_name="about.html"

# class Coin:
#     def __init__(self, type, year, value, image, quantity):
#         self.type = type
#         self.year = year
#         self.value = value
#         self.image = image
#         self.quantity = quantity

# coins = [
#     Coin("Washington Head Quarter", "1934", "twenty-five Cents", "https://www.images-apmex.com/images/products/1934-washington-quarter-good-vf_12352_Obv.jpg?v=20130101120000&width=900&height=900", "11"),
#     Coin("Washington Head Quarter", "1935", "twenty-five Cents", "https://www.images-apmex.com/images/products/1935-d-washington-quarter-good-vg_12355_Obv.jpg?v=20130101120000&width=900&height=900", "13" )
# ]

class CoinList(TemplateView):
    template_name = "coin_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coins'] = Coin.objects.all()
        return context
