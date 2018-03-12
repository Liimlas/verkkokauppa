from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^play/$', views.play, name='play'),
    url(r'^play/([a-zA-Z0-9]+)/$', views.playgame, name='play'),
    url(r'^play/[a-zA-Z0-9]+/save_scores/$', views.save_scores, name='save_scores'),
    url(r'^play/[a-zA-Z0-9]+/save_state/$', views.save_state, name='save_state'),
    url(r'^play/[a-zA-Z0-9]+/load_state/$', views.load_state, name='load_state'),
]
