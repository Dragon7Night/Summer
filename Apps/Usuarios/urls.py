
from django.urls import path

from Apps.Usuarios.views import *

urlpatterns = [

    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('log-in/', LogInView.as_view(), name='log_in'),


]
