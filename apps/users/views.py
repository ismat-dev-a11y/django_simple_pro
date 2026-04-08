from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from apps.notes.models import Note
from django.contrib.auth import logout

class SimplePage(generic.ListView):
    model = Note
    template_name = 'simple.html'


class RegisterView(generic.CreateView):
  form_class = RegisterForm
  success_url = reverse_lazy('login')
  template_name = 'register.html'

class Login_View(LoginView):
  form_class = LoginForm
  template_name = 'login.html'
  success_url = reverse_lazy('notes:notes')

def logout_view(request):
  logout(request)
  return redirect('login')