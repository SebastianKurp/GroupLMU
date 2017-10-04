from django.conf.urls import url, include
from . import views

app_name = 'notes'

urlpatterns = [
    # /notes/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /notes/71
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /notes/note/create
    url(r'note/create/$', views.NoteCreate.as_view(), name='note-create'),
]


