from django.conf.urls import patterns, url
from pastebin import views
#from django.views.generic.create_update import create_object

urlpatterns = patterns('',
    url(r'^$', views.ObjectList.as_view()),
    url(r'^(?P<object_id>\d+)/$', views.ObjectDetail.as_view(), name='object_detail'),
    url(r'^add/$', views.CreateObject.as_view()),
)
