from django import template
from .search import search
from .report_by_symbol import reportBySymbol
from .test_search import showResult

register = template.Library()

@register.filter(name='get_note_contents')
def get_note_contents(value):
    return value[:20] + "..."

# get_note_contents currently just
# outputs a shortened version of the note's contents


@register.simple_tag(name="search_word")
def search_word(note, keyword):
    note_with_line_split = note.content+"\n"
    print(note_with_line_split)
    searchResults = search(note_with_line_split, note.title, keyword, 30)
    if len(searchResults) == 0:
        return "Unable to return exact instance of search result. Please click title for full contents."
    else:
        return searchResults[0][1] #first hit, 0th index is title

@register.simple_tag(name="symbol_search")
def symbol_search(note, symbol):
    note_with_line_split = note.content+"\n"
    searchResults = reportBySymbol(note_with_line_split, note.title, symbol, 30, style="by symbol")
    return searchResults