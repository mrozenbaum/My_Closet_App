from django.conf.urls import url

from . import views

app_name="mycloset"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_owner/$', views.new_owner, name='new_owner'),
]