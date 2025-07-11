from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('popular_notes', views.PopularNotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
]
