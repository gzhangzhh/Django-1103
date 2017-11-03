# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),
    url(r'^info/$',views.info),
    url(r'^order/$',views.order),
    url(r'^site/$',views.site),
]