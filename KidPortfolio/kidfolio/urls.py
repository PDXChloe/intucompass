from django.conf.urls import url
from kidfolio import views

app_name = 'kidfolio'
urlpatterns = [
    #url(r'^$', views.index, name="index"),
    url(r'^$', views.index, name="index"),
    url(r'^get_portfolios/$', views.get_portfolios, name="get_portfolios"),
    url(r'^new_kidpost/$', views.new_kidpost, name="new_kidpost"),
    url(r'^new_portfolio/$', views.new_portfolio, name="new_portfolio"),
    url(r'^publish_new_kidpost/$', views.publish_new_kidpost, name="publish_new_kidpost"),
    url(r'^create_portfolio/$', views.create_portfolio, name="create_portfolio"),
    url(r'^edit_kidpost/(?P<kid_id>[0-9]+)$', views.edit_kidpost, name='edit_kidpost'),
    url(r'^get_kidpost/(?P<kid_id>[0-9]+)$', views.get_kidpost, name='get_kidpost'),
    url(r'^new_user/$', views.new_user, name='new_user'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^get_this_portfolio/(?P<portfolio_id>[0-9]+)$', views.get_this_portfolio, name='get_this_portfolio'),

]