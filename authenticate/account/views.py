from typing import Any, Dict
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import *



class LoginPage(LoginView):
    redirect_authenticated_user = True

    template_name = 'authenticate/login.html'

    def get_success_url(self):
        return reverse_lazy('home')



class IndexPage(ListView):
    model = Student
    template_name = 'authenticate/index.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['students'] = context['students'].filter(index_number=self.request.user)
        return context


class RegisterPage(FormView):
    form_class = UserCreationForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(self,*args, **kwargs)