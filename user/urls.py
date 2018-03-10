from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/([-\w]+)/$', views.viewUser, name='user'),
    url(r'^profile/update_profile/(?P<pk>\d+)/$',
        views.update_profile,
        name='update_profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profiles/$', views.profiles, name='profiles'),
    url(r'^account_activation_sent/$',
        views.activation_sent,
        name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate,
        name='activate'),
    url(r'^manage_games/$', views.manage_games, name='manage_games'),
    url(r'^manage_games/([a-zA-Z0-9]+)/$', views.edit_game,
        name='manage_games'),
    url(r'^managed_game/$', views.edit, name='managed_game'),
    url(r'^delete_game/$', views.delete_game, name='delete_game'),

]
