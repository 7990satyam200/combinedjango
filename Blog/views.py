from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import News
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from .forms import SignUpForm
# from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BlogHome(ListView):
    template_name='Blog_list.html'
    model=News


class Detail(DetailView):
    model=News
    template_name = 'blog_detail.html'


class new( CreateView):
    model=News
    template_name = 'blog_new.html'
    fields='__all__'



class editView(UpdateView):
    model = News
    template_name ='blog_new.html'
    fields='__all__'

class deleteView(DeleteView):
    model = News
    template_name = 'news_confirm_delete.html'
    success_url = reverse_lazy('Blog')

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})
