from django.contrib import admin
from .models import Coin, CoinComment
# Register your models here.
admin.site.register(Coin)
admin.site.register(CoinComment)