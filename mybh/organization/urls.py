from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.organization_menu, name='organization_menu'),
    url(r'organization_list/$', views.organization_list, name='organization_list')
]