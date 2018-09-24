from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^create_job$', views.create_job),
    url(r'^delete_job/(?P<id>\d+)$', views.delete_job),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^help/(?P<id>\d+)$', views.help),
    url(r'^complete/(?P<id>\d+)$', views.complete),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
]
