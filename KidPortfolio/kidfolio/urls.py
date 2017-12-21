from django.conf.urls import url
from kidfolio import views

app_name = 'kidfolio'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new_kidpost/$', views.new_kidpost, name="new_kidpost"),
    url(r'^publish_new_kidpost/$', views.publish_new_kidpost, name="publish_new_kidpost"),
]