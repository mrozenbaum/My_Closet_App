from django.conf.urls import url

from . import views

app_name="mycloset"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /mycloset/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /mycloset/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /mycloset/5/item_views/
    url(r'^(?P<owner_id>[0-9]+)/item_view/$', views.ItemViewView, name='item_view'),
    # page for adding a new owner profile (form)
    url(r'^new_owner/$', views.new_owner, name='new_owner'),
    # page for adding a new item
    url(r'^new_item/(?P<owner_id>\d+)/$', views.new_item, name='new_item'),
    # editing Owner profile view
    url(r'^edit_owner/(?P<owner_id>\d+)/$', views.edit_owner, name='edit_owner'),
    # editing item information view
    url(r'^edit_item/(?P<item_id>\d+)/$', views.edit_item, name='edit_item'),
    # ex: /mycloset/5/like/
    url(r'^(?P<owner_id>[0-9]+)/like/$', views.like, name='like'),
]
    
