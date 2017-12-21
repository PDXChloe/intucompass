from django.conf.urls import url
from kidfolio import views

app_name = 'kidfolio'
urlpatterns = [
    #url(r'^$', views.index, name="index"),
    url(r'^$', views.get_portfolios, name="index"),
    url(r'^new_kidpost/$', views.new_kidpost, name="new_kidpost"),
    url(r'^publish_new_kidpost/$', views.publish_new_kidpost, name="publish_new_kidpost"),
    url(r'^edit_kidpost/$', views.edit_kidpost, name='edit_kidpost'),
    url(r'^get_kidpost/(?P<kid_id>[0-9]+)$', views.get_kidpost, name='get_kidpost'),
]