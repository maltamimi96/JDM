from django.conf.urls import url
from . import views
from django.urls import include, path


urlpatterns = [
    path(r'^$', views.car_new),
]
