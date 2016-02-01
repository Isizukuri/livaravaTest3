from django.contrib import admin
from models import TextNote, Book
from forms import TextNoteForm


class TextNoteAdmin(admin.ModelAdmin):
    form = TextNoteForm

admin.site.register(TextNote, TextNoteAdmin)
admin.site.register(Book)
