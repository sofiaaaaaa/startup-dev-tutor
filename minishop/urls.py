from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'shopping.views.index'),
	url(r'product/(?P<resource_id>\d+)', 'shopping.views.show'),
	url(r'comment/create', 'shopping.views.comment'),
	url(r'comment/delete/(?P<resource_id>\d+)', 'shopping.views.delete_comment'),
    # Examples:
    # url(r'^$', 'minishop.views.home', name='home'),
    # url(r'^minishop/', include('minishop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
