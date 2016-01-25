from models import TextNote


def note_count_processor(request):
    """Context processor for count of text notes"""
    return {'notes_count': TextNote.objects.count()}
