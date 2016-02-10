from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.actions import delete_selected

from models import TextNote, Book
from forms import TextNoteForm


class BulkDeleteMixin(object):
    class SafeDeleteQuerysetWrapper(object):
        def __init__(self, wrapped_queryset):
            self.wrapped_queryset = wrapped_queryset

        def _safe_delete(self):
            for obj in self.wrapped_queryset:
                obj.delete()

        def __getattr__(self, attr):
            if attr == 'delete':
                return self._safe_delete
            else:
                return getattr(self.wrapped_queryset, attr)

        def __iter__(self):
            for obj in self.wrapped_queryset:
                yield obj

        def __getitem__(self, index):
            return self.wrapped_queryset[index]

        def __len__(self):
            return len(self.wrapped_queryset)

    def get_actions(self, request):
        actions = super(BulkDeleteMixin, self).get_actions(request)
        actions['delete_selected'] = (
            BulkDeleteMixin.action_safe_bulk_delete,
            'delete_selected',
            _("Delete selected %(verbose_name_plural)s")
            )
        return actions

    def action_safe_bulk_delete(self, request, queryset):
        wrapped_queryset = BulkDeleteMixin.SafeDeleteQuerysetWrapper(queryset)
        return delete_selected(self, request, wrapped_queryset)


class TextNoteAdmin(BulkDeleteMixin, admin.ModelAdmin):
    form = TextNoteForm


class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('note',)

admin.site.register(TextNote, TextNoteAdmin)
admin.site.register(Book, BookAdmin)
