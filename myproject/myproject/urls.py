from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','main.views.index',name="index"),
    url(r'^angular/$','angular.views.angularindex',name="angularindex"),
    url(r'^angular1/$','angular.views.angular1',name="angular1"),
    url(r'^angular4/$','angular.views.angular4',name="angular4"),
    url(r'^vuejs/$','vuejs.views.index',name="vuejsindex"),
    url(r'^react/$','react.views.index',name="reactindex"),
    
    
)
