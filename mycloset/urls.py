from django.conf.urls import url

from . import views

app_name="mycloset"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # page for adding a new owner profile (form)
    url(r'^new_owner/$', views.new_owner, name='new_owner'),
    # page for viewing a owners profile
    url(r'^owner_profile/$', views.owner_profile, name='owner_profile'),
    # ex: /mycloset/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /mycloset/5/like/
    url(r'^(?P<owner_id>[0-9]+)/like/$', views.like, name='like'),
    # ex: /mycloset/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]
    
