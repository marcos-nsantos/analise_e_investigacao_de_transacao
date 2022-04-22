from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class UsuarioLoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('usuario:index')
