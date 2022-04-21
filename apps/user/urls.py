from django.urls import path

from .views.cadastro_view import CadastroCreateView

app_name = 'user'
urlpatterns = [
    path('cadastro/', CadastroCreateView.as_view(), name='cadastro'),
]
