from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^payment/([a-zA-Z0-9]+)/$', views.payment, name="payment"),
]
