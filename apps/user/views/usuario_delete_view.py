from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, reverse

from ..models.user_model import User


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user:lista')
    template_name = 'user/deletar_usuario.html'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        user = super().get_object()
        if user.is_superuser:
            raise Http404
        return user

    def get_success_url(self):
        messages.success(self.request, 'Usuário deletado com sucesso!')
        return reverse('user:lista')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id == request.user.id:
            messages.warning(self.request, 'Você não pode deletar a si mesmo!')
            return redirect('user:lista')
        return super().dispatch(request, *args, **kwargs)
