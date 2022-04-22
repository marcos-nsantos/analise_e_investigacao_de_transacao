from django.views.generic import ListView

from ..models.user_model import User


class UsuariosListView(ListView):
    model = User
    template_name = 'user/listagem_usuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.all()
