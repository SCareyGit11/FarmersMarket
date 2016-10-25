<<<<<<< HEAD
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
=======
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^results$', views.results)
>>>>>>> 146fd5965a83c3e0c64ed5f2be3265633cd7d25d
]
