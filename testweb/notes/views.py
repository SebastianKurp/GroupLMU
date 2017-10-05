from django.views import generic
from .models import note
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'all_notes'

    def get_queryset(self):
        return note.objects.all()


class DetailView(generic.DetailView):
    model = note
    #'note' here is the variable you use to reference an individual note
    #in details.html
    template_name = 'notes/detail.html'

class NoteCreate(CreateView):
    model = note
    fields = [
        'title',
        'content'
    ]