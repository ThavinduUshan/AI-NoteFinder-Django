from django.urls import path
from .views import notes, search

urlpatterns = [
    path('', notes, name='note_list'),
    path('search/', search, name='search_notes'),
]
