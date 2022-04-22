from django.urls import path

from .views.cadastro_view import CadastroCreateView
from .views.usuarios_list_view import UsuariosListView

app_name = 'user'
urlpatterns = [
    path('cadastro/', CadastroCreateView.as_view(), name='cadastro'),
    path('lista/', UsuariosListView.as_view(), name='lista'),
]
