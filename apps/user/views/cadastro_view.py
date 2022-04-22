from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from ..models.user_model import User
from ..forms.sign_up_form import SignUpForm


class CadastroCreateView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'user/cadastro.html'
    success_url = reverse_lazy('user:login')
    __password = None

    def form_valid(self, form):
        self.__password = self.generate_random_password()
        self.save_user(form, self.__password)
        self.send_email(form.instance)
        return super().form_valid(form)

    def save_user(self, form, password):
        user = form.save(commit=False)
        user.set_password(password)
        user.save()

    def generate_random_password(self, length=6):
        random_password = self.model.objects.make_random_password(length=length)
        return random_password

    def send_email(self, user):
        try:
            subject = 'Bem vindo ao sistema de transações'
            message = render_to_string('user/welcome_email.html', {
                'email': user.email,
                'password': self.__password
            })
            message_html = strip_tags(message)
            from_email = settings.EMAIL_HOST_USER
            to_email = [user.email]
            send_mail(subject, message_html, from_email, to_email, html_message=message)
        except Exception as e:
            raise e
