from django.urls import path

from .views.cadastro_view import CadastroCreateView
from .views.usuarios_list_view import UsuariosListView
from .views.usuario_delete_view import UsuarioDeleteView
from .views.usuario_updated_view import UsuarioUpdateView

app_name = 'user'
urlpatterns = [
    path('cadastro/', CadastroCreateView.as_view(), name='cadastro'),
    path('lista/', UsuariosListView.as_view(), name='lista'),
    path('delete/<int:pk>/', UsuarioDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', UsuarioUpdateView.as_view(), name='update'),
]
