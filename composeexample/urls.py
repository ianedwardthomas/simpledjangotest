from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from test import views as test_views

urlpatterns = [
    url('^accounts/login/', auth_views.login),
    url('^test/', test_views.page),
    url(r'^admin/', include(admin.site.urls)),
]
