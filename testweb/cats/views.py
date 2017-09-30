from .models import adorable_kitten
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_kittens = adorable_kitten.objects.all()
    context = {'all_kittens': all_kittens}
    return render(request, 'cats/index.html', context)


def detail(request, kitten_id):
    try:
        kitten = adorable_kitten.objects.get(id=kitten_id)
    except adorable_kitten.DoesNotExist:
        raise Http404("No kitten here.")
    return render(request, 'cats/detail.html', {'kitten': kitten})