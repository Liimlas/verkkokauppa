from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/([a-zA-Z0-9]+)/$', views.viewUser, name='user'),
    url(r'^profile/update_profile/(?P<pk>\d+)/$', views.update_profile, name='update_profile'),
    #url(r'^profile_updated/$', views.profile_updated, name='profile_updated'),
    url(r'^upload/$', views.model_form_upload, name='upload'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profiles/$', views.profiles, name='profiles'),
    url(r'^manage_games/$', views.manage_games, name='manage_games'),
    #url(r'^manage_games/(?P<pk>\d+)/$', views.edit_game, name='manage_games'),
    url(r'^manage_games/([a-zA-Z0-9]+)/$', views.edit_game, name='manage_games'),
    #url(r'^update_game/(?P<pk>\d+)/$', views.edit_game, name='update_game'),
    url(r'^managed_game/$', views.edit, name='managed_game'),
]
