from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login

app_name = 'notes'

urlpatterns = [
    # /notes/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /notes/[primary key]
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /notes/note/create
    url(r'note/create/$', views.NoteCreate.as_view(), name='note-create'),

    # /notes/note/[primary key]
    url(r'note/(?P<pk>[0-9]+)/$', views.NoteUpdate.as_view(), name='note-update'),

    # /notes/note/[primary key]/delete
    url(r'note/(?P<pk>[0-9]+)/delete/$', views.NoteDelete.as_view(), name='note-delete'),

    # /notes/signup
    url(r'^signup/$', views.UserFormView.as_view(), name='signup'),

    # /notes/login
    url(r'^login/$', login, {'template_name': 'notes/login.html'})
]


