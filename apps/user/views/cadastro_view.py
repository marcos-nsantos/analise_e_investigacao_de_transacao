from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..models.user_model import User
from ..forms.sign_up_form import SignUpForm


class CadastroCreateView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'user/cadastro.html'
    success_url = reverse_lazy('transacao:index')
