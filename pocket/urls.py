from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'list_pocket.views.list_status', name='list_status'),
    url(r'^twitter/login/$', 'list_pocket.views.twitter_login', name="twitter_login"),
    url(r'^twitter/callback/$', "list_pocket.views.twitter_callback", name="twitter_callback"),
)
