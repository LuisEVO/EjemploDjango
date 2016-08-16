from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from .models import *

class AuthorList(ListView):
    model = Author
    template_name = 'app/author/list.html'

class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'app/author/form.html'
    success_url = reverse_lazy('app:author-list')

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'app/author/form.html'
    success_url = reverse_lazy('app:author-list')

class AuthorDetail (DetailView):
    model = Author
    fields = ['name']
    template_name = 'app/author/detail.html'

class AuthorDelete(DeleteView):
    model = Author
    template_name = 'app/author/confirm_delete.html'
    success_url = reverse_lazy('app:author-list')
