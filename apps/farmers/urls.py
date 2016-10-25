from django.conf.urls import url, include
from views import index,show_fMarket
from ..login_reg_app.views import login, register, success, logout

urlpatterns = [
    url(r'^$', index),
    url(r'^main$', show_fMarket),
    url(r'^login$', login),
    url(r'^register$', register),
    url(r'^success$', success),
    url(r'^logout$', logout),
]
