from django.urls import path
from .views import *
app_name = 'notes'
urlpatterns = [
    path('all-notes/', NoteList.as_view(), name='all-notes'),
    path('notes/', NoteListView.as_view(), name='notes'),
    path('create/', NoteCreateView.as_view(), name='create'),
    path('update/<int:pk>', NoteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', NoteDetailView.as_view(), name='detail'),

]
