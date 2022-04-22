from django.http import Http404
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from ..models.user_model import User
from ..forms.update_form import UserUpdateForm


class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/update_usuario.html'
    success_url = reverse_lazy('user:lista')
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        user = super().get_object()
        if user.is_superuser:
            raise Http404
        return user
