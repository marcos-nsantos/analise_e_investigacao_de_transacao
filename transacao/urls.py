from django.urls import path

from .views import index_view

app_name = 'transacao'
urlpatterns = [
    path('', index_view.index, name='index'),
]
