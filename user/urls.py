from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profiles/$', views.profiles, name='profiles'),
    url(r'^manage_games/$', views.manage_games, name='manage_games'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
]
