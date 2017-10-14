from django.contrib.auth.models import User
from django.template import RequestContext
from django.views import generic
from .models import note
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'all_notes'

    def get_queryset(self):
        return note.objects.all()


class DetailView(generic.DetailView):
    model = note
    # 'note' here is the variable you use to reference an individual note
    # in details.html
    template_name = 'notes/detail.html'


def page_not_found(request):
    response = render_to_response('404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response


class NoteCreate(CreateView):
    model = note
    fields = [
        'title',
        'content'
    ]
    # form_valid override to make sure that
    # foreign key of user signed in is assigned to note
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(UpdateView):
    model = note
    fields = [
        'title',
        'content'
    ]


class NoteDelete(DeleteView):
    model = note
    success_url = reverse_lazy('notes:index')
    # reverse_lazy redirects to index.html upon note
    # deletion


class UserFormView(View):
    form_class = UserForm
    #references UserForm in forms.py
    template_name = 'notes/signup.html'

    # blank form for new users
    def get(self, request):
        form = self.form_class(None)
        # form_class is variable above which is UserForm
        # from forms.py
        return render(request, self.template_name, {'form': form})

    # handle user signup data upon POST
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # create an object but do not
            # save it immediately
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # passwords are hashed by django so cannot
            # be referenced directly as user.attribute
            # must use set method
            user.save()
            #save to DB

            # if username/pass are accurate, return User object
            user = authenticate(username=username, password=password)

            if user is not None:
                #if they exist in DB
                if user.is_active:
                    #if they are not invalidated
                    login(request, user)
                    return redirect('notes:index')
                    # redirect to index upon succesful login
        else:
            return render(request, 'notes/bad_form.html', {'form':form})
            #if they enter bad signup info, take them to a page that tells them so

def search_form(request):
    return render(request, 'notes/search-form.html')


def search(request):
    if 'q' in request.GET:
        q = request.GET['q'] #store query in variable
        notes = note.objects.filter(content__icontains=q)
        count = notes.count();
        return render(request, 'notes/search_results.html', {'notes':notes, 'query':q, 'count':count})
    else:
        message = "Fill out the form next time."
    return HttpResponse(message)