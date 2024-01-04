from django.urls import include, path
from .views import usuario_views

urlpatterns = [
    path('cadastrar_usuario/', usuario_views.UsuarioList.as_view(), name='usuario-list'),



]
