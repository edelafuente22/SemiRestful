from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='users'),
    url(r'^/new$', views.new, name='new'),
    url(r'^/(?P<id>\d+)/edit$', views.edit, name='edit'),
    url(r'^/(?P<id>\d+)$', views.show, name='show'),
    url(r'^/create$', views.create, name='create'),
    url(r'^/(?P<id>\d+)/delete$', views.delete, name='delete'),
    url(r'^/(?P<id>\d+)/update$', views.update, name='update'),
]


# url(r'^$', views.toindex, name='my_index'),
#     url(r'^this_app/new$', views.new, name='my_new'),
#     url(r'^this_app/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
#     url(r'^this_app/(?P<id>\d+)/delete$', views.delete, name='my_delete'),
#     url(r'^this_app/(?P<id>\d+)$', views.show, name='my_show'),