from django.urls import path
from .views import note_list, search_notes, category_list

urlpatterns = [
    path('', note_list, name='note_list'),
    path('search/', search_notes, name='search_notes'),
    path('categories/', category_list, name='category_list'),
]
