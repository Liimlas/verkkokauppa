from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^play/$', views.play, name='play'),
    url(r'^play/([a-zA-Z0-9]+)/$', views.playgame, name='play'),
    url(r'^play/[a-zA-Z0-9]+/save_scores/$', views.save_scores, name='save_scores')
]
