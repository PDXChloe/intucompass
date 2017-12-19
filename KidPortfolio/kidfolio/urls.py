from django.conf.urls import url
from kidfolio import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]