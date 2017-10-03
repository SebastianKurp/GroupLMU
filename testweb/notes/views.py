from .models import note, mention
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_notes = note.objects.all()
    context = {'all_notes': all_notes}
    return render(request, 'notes/index.html', context)


def detail(request, note_id):
    try:
        a_note = note.objects.get(id=note_id)
    except note.DoesNotExist:
        raise Http404("No kitten here.")
    return render(request, 'notes/detail.html', {'a_note': a_note})


def favorite(request, note_id):
    a_note = note.objects.get(id=note_id)
    try:
        selected_mention = a_note.mention_set.get(pk=request.POST['mention'])
    except(KeyError, mention.DoesNotExist):
        return render(request, 'notes/detail.html', {
            'a_note': a_note,
            'error_msg': "Invalid human selection",
        })
    else:
        if selected_mention.is_favorite:
            selected_mention.is_favorite = False
            # if the note is already favorited, clicking again will 'unfavorite'
        else:
            selected_mention.is_favorite = True
        selected_mention.save()
        return render(request, 'notes/detail.html', {'a_note': a_note})
