from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy

class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    # login_url = 'login'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class NoteList(generic.ListView):
    model = Note
    template_name = 'notes/all_note.html'
    context_object_name = 'NOTES'

    def get_queryset(self):
        return Note.objects.all()

class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/notes_create.html'
    success_url = reverse_lazy('notes:notes')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/notes_update.html'
    success_url = reverse_lazy('notes:notes')

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    success_url = reverse_lazy('notes:notes')
    template_name = 'notes/notes_delete.html'

class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)