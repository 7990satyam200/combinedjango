from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, View, TemplateView
# from django.template import RequestContext
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from . models import post
from django.urls import reverse_lazy
# from django.contrib.auth import authenticate, login
# from django.template import RequestContext
# from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin


class socialListView(ListView):
    model  = post
    template_name ='tweet.html'

class Profile(TemplateView):
    model  = post
    template_name ='detail.html'


class twitDetailView(DetailView):
    model = post
    template_name = 'tweet_detail.html'


# class new_tweet(CreateView):
#     model = twit
#     template_name = 'twit_form.html'
#     fields = ['tweet', 'profile']

class new_tweet(LoginRequiredMixin, CreateView): # new
    model = post
    template_name = 'twit_form.html'
    fields = ['tweet', 'profile']
    login_url = 'login' # new

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class twitEditView(UpdateView):
    model = post
    template_name = 'twitEditView.html'
    fields = ['tweet', 'profile']


class twitDeleteView(DeleteView):
    model = post
    template_name = 'tweet_delete.html'
    success_url= reverse_lazy('social')

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
