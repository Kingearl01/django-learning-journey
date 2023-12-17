from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
# Create your views here.
class IndexView(ListView):
    model = Software
    context_object_name = 'softwares'
    template_name = 'software/index.html'

class SoftwareDetailView(DetailView):
    model = Software
    # context_object_name = 'softwares'