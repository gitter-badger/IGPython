from django.conf.urls import patterns, include, url
from sources.views import SourcesList, SourcesView, SourceCreate, SourceUpdate, delete_source
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(SourcesList.as_view()), name='sources_list'),
    url('^(?P<pk>\d+)/$', SourcesView.as_view(), name='source_details'),
    url('^create/$', SourceCreate.as_view(), name='source_create'),
    url(r'^(?P<pk>\d+)/update/$', SourceUpdate.as_view(), name='source_update'),
    url(r'^(?P<source_id>\d+)/delete/$', delete_source, name='source_delete'),
)