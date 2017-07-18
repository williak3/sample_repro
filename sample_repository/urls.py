#from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'sample_repository.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
