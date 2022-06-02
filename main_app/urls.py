from django.urls import path
from . import views

urlpatterns =[
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('coins/', views.CoinList.as_view(), name="coins"),
    path('coins/new/', views.CoinCreate.as_view(), name="coin_create"),
    path('coins/<int:pk>/', views.CoinDetail.as_view(), name="coin_detail"),
    path('coins/<int:pk>/update', views.CoinUpdate.as_view(), name="coin_update"),
    path('coins/<int:pk>/delete', views.CoinDelete.as_view(), name="coin_delete"),
    path('comment/new/', views.CommentCreate.as_view(), name="comment_create"),
]