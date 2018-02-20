from main.models import Game
from django.shortcuts import render, redirect


def index(request):
    game_list = games_by_attribute(Game.objects.all(), 4, True)
    three_newest = games_by_attribute(Game.objects.all(), 4, True)
    three_newest = three_newest[:3]
    context = {'games':game_list}
    context['three_newest'] = three_newest
    return render(request, 'frontpage/index.html', context)


# Gives a sorted list back according to a given attribute. e.g. amount of sold copies or price, etc
def games_by_attribute(gamelist, attribute, reversed):
    games_sorted = []
    for game in gamelist:
        games_sorted.append(game)

    if(attribute == 0): #Sort by name
        games_sorted.sort(key=lambda x: x.name, reverse=reversed)
    elif(attribute == 1): #Sort by price
        games_sorted.sort(key=lambda x: x.price, reverse=reversed)
    elif(attribute == 2): #Sort by soldcopies
        games_sorted.sort(key=lambda x: x.soldcopies, reverse=reversed)
    elif(attribute == 3): #Sort by sale price
        games_sorted.sort(key=lambda x: x.saleprice, reverse=reversed)
    elif(attribute == 4): #Sort by publish date
        games_sorted.sort(key=lambda x: x.publish_date, reverse=reversed)

    return games_sorted



