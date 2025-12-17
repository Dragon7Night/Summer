from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView 


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('log_in')
    template_name = 'Ingreso/registro.html'



class LogInView(LoginView):

    template_name = 'Ingreso/iniciar_sesion.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    # en caso de que el usuario este autentificado se redirecciona al home
    def get_success_url(self):
        return reverse_lazy('home_main')




