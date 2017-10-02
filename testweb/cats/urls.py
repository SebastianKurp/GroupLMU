from django.conf.urls import url
from . import views

app_name = 'cats'

urlpatterns = [
    # /cats/
    url(r'^$', views.index, name='index'),

    # /cats/71
    url(r'^(\d+)/$', views.detail, name='detail'),

    # /cats/favorite
    url(r'^(?P<a_note_id>[0-9]+)/favorite/$', views.favorite, name='favorite')

]
