from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from users.forms import UserForm
from users.models import Users

def user_list (request):
    data={

        'title' : 'Listado de Usuarios',
        'users' : Users.objects.all()
    }
    return render (request,'users/user_list.html', data)

class User_listView(ListView):
    model = Users
    template_name = 'users/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        return context
    

class User_createView(CreateView):
    model = Users
    form_class = UserForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Usuarios'
        return context