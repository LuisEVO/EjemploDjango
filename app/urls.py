from django.conf.urls import url
from .views import *

app_name = 'app'
urlpatterns = [
    url(r'^create/$', AuthorCreate.as_view(), name='author-create'),
    url(r'^update/(?P<pk>\d+)/$', AuthorUpdate.as_view(), name='author-update'),
    url(r'^detail/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^list/$', AuthorList.as_view(), name='author-list'),
    url(r'^delete/(?P<pk>\d+)/$', AuthorDelete.as_view(), name='author-delete'),

]