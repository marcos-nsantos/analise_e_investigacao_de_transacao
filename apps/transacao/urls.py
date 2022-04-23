from django.urls import path

from .views.index_view import TransacaoView
from .views.transacao_detail_view import TransacaoDetailView

app_name = 'transacao'
urlpatterns = [
    path('', TransacaoView.as_view(), name='index'),
    path('<int:pk>/', TransacaoDetailView.as_view(), name='detail'),
]
