from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^games/$', views.games, name='games'),
    url(r'^games/([a-zA-Z0-9]+)/$', views.viewgame, name='games'),
]
