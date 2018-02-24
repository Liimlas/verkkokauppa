from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^payment/success/([a-zA-Z0-9]+)/$',
        views.success,
        name="payment_success"),
    url(r'^payment/error/$', views.cancel, name="payment_cancel"),
    url(r'^payment/cancel/$', views.error, name="payment_error"),
    url(r'^payment/([a-zA-Z0-9]+)/$', views.payment, name="payment"),
]
