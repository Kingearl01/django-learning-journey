from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView

from .models import Post
# Create your views here.

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    # redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)


class BlogLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'blog/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/create.html'
    success_url = reverse_lazy('home')

class IndexView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'blog/index.html'

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'blog/detail.html'

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'blog/blog_form.html'

    success_url = reverse_lazy('home')


class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'blog/delete_blog.html'

    success_url = reverse_lazy('home')