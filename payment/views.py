from django.shortcuts import render, redirect
from main.models import Game, BoughtGame
from django.core.exceptions import ObjectDoesNotExist
from hashlib import md5
from main.models import BoughtGame, Game
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def payment(request, gameid):
    try:
        game = Game.objects.get(id=gameid)
    except ObjectDoesNotExist:
        return redirect('error')

    alreadyOwned = True
    ownedSet = BoughtGame.objects.filter(owner=request.user, game=game)

    if ownedSet.count() == 0 and game.developer != request.user:
        alreadyOwned = False

    if game.onsale:
        amount = game.saleprice
    else:
        amount = game.price

    sid = 'SteamWsdAikaLoppuuSOS'
    secret_key = '14d8e062330c3ed6e565d43141ce4999'
    success_url = 'http://localhost:8000/payment/success/'
    cancel_url = 'http://localhost:8000/payment/cancel/'
    error_url = 'http://localhost:8000/payment/error/'
    pid = 'HienoOstosTosiHienoa'
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()

    context = {
        'game': game,
        'alreadyOwned': alreadyOwned,
        'price': amount,
        'pid': pid,
        'sid': sid,
        'success_url': success_url,
        'cancel_url': cancel_url,
        'error_url': error_url,
        'checksum': checksum,
        }
    return render(request, 'payment/payment.html', context)


@login_required
def error(request):
    return render(request, 'payment/payment_error.html')

@login_required
def success(request, gameid):
    user = request.user
    boughtGame = Game.objects.get(id=gameid)

    oldPurchase = BoughtGame.objects.filter(owner=user, game=boughtGame)
    if oldPurchase.count() != 0:
        return redirect('games')

    newPurchase = BoughtGame(owner=user, game=boughtGame)
    newPurchase.save()
    context = {'game': boughtGame}
    return render(request, 'payment/payment_success.html', context)


@login_required
def cancel(request):
    return render(request, 'payment/payment_cancel.html')