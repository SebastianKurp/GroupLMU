from .models import adorable_kitten, human
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


def favorite(request, kitten_id):
    kitten = adorable_kitten.objects.get(id=kitten_id)
    try:
        selected_human = kitten.human_set.get(pk=request.POST['human'])
    except(KeyError, human.DoesNotExist):
        return render(request, 'cats/detail.html', {
            'kitten': kitten,
            'error_msg': "Invalid human selection",
        })
    else:
        if selected_human.is_favorite:
            selected_human.is_favorite = False
            # if the note is already favorited, clicking again will 'unfavorite'
        else:
            selected_human.is_favorite = True
        selected_human.save()
        return render(request, 'cats/detail.html', {'kitten': kitten})
