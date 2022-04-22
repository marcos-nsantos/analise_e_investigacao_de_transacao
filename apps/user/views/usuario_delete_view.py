from django.http import Http404
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from ..models.user_model import User


class UsuarioDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user:lista')
    template_name = 'user/deletar_usuario.html'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        user = super().get_object()
        if user.is_superuser:
            raise Http404
        return user
