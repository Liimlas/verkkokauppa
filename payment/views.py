from django.shortcuts import render, redirect
from main.models import Game, BoughtGame


def payment(request, gameid):
    game = Game.objects.get(id=gameid)
    price = 0
    if game.onsale:
        price = game.saleprice
    else:
        price = game.price
    context = {'game': game, 'price': price}
    return render(request, 'payment/payment.html', context)