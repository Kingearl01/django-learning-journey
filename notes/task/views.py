from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

# Create your views here.
class RegisterPage(FormView):
    form_class = UserCreationForm
    template_name = 'task/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(self, *args, **kwargs)

class LoginPage(LoginView):
    redirect_authenticated_user = True
    template_name = 'task/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


class CreateTask(CreateView):
    model = Task
    template_name = 'task/create.html'
    fields = ['title', 'description', 'status']
    exclude = 'user'
    success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(CreateTask, self).form_valid(form)


class IndexPage(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        print(context['tasks'])
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/update.html'
    fields = "__all__"
    
    success_url = reverse_lazy('home')


    
class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete_confirm.html'
    success_url = reverse_lazy('home')