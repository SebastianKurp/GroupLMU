from django.conf.urls import url
from . import views

urlpatterns = [
    # /cats/
    url(r'^$', views.index, name='index'),
    # /cats/71
    url(r'^(\d+)/$', views.detail, name='detail')

]
