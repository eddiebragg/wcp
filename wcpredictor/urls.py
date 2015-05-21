from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from wcpredictor.wcp import views


router = routers.DefaultRouter()
router.register(r'user-profiles', views.UserProfileViewSet)

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
                       url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^admin/', include(admin.site.urls)),
                       )
