from django.contrib import admin
from models import TextNote
from forms import TextNoteForm


class TextNoteAdmin(admin.ModelAdmin):
    form = TextNoteForm

admin.site.register(TextNote, TextNoteAdmin)
