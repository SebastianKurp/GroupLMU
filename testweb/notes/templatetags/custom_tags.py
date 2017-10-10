from django import template
from .search import search
from .report_by_symbol import reportBySymbol
from .test_search import showResult

register = template.Library()

@register.filter(name='get_note_contents')
def get_note_contents(value):
    return value[:10] + "..."

# get_note_contents currently just
# outputs a shortened version of the note's contents


@register.filter(name='get_note')
def get_note(note):
    searchResults = search(note.content, note.title, "cat", 10)
    print("Content: " + note.content + " Title: " +  note.title)
    result = showResult("Testing...", searchResults)
    print(searchResults)
    return result