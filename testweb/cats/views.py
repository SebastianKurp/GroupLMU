from django.shortcuts import render
from django.http import HttpResponse
from .models import adorable_kitten
from django.template import loader


def index(request):
    all_kittens = adorable_kitten.objects.all()
    template = loader.get_template("cats/index.html")
    context = {
        'all_kittens': all_kittens,

    }
    return HttpResponse(template.render(context, request))


def detail(request, kitten_id):
    return HttpResponse("<h2>Details for : " + str(kitten_id) + "</h2>")
