from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^games/$', views.games, name='games'),
    url(r'^games/([a-zA-Z0-9]+)/$', views.viewgame, name='games'),
    url(r'^addGame/$', views.addGame, name='addGame'),
    url(r'^onSale/$', views.onSale, name='onSale'),
]

