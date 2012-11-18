from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bottle.views.home', name='home'),
    # url(r'^bottle/', include('bottle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^polls/$', 'polls.views.index'),
     url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
     url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
     url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^describe/$', 'describe.views.index'),
     url(r'^describe/submit$', 'describe.views.submit')
)
