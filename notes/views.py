from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from . models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/popular_notes.html"
    queryset = Notes.objects.filter(likes__gte=1)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "notes"
