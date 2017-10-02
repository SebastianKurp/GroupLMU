from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    # /notes/
    url(r'^$', views.index, name='index'),

    # /notes/71
    url(r'^(\d+)/$', views.detail, name='detail'),

    # /notes/favorite
    url(r'^(?P<a_note_id>[0-9]+)/favorite/$', views.favorite, name='favorite')

]
