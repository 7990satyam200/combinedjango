from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, View, TemplateView
from django.template import RequestContext
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from .forms import SignUpForm

# Create your views here.
from django.views.generic import TemplateView
class home(TemplateView):
    template_name='index.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
