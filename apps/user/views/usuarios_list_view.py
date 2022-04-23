from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models.user_model import User


class UsuariosListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/listagem_usuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.filter(is_superuser=False, is_active=True)
