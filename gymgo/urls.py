from django.urls import include, re_path, path
from .views import planos_views, usuario_views

urlpatterns = [
    # Paths de usuarios e login
    path('cadastro/', usuario_views.cadastro, name='cadastro'),
    path('login/', usuario_views.login, name='login'),
    path('logout/', usuario_views.logout, name='logout'),
    path('teste_token/', usuario_views.test_token, name='teste_token'),
    path('perfil_cadastro/', usuario_views.perfil_cadastro, name='perfil_cadastro'),
    path('perfil_usuario/', usuario_views.perfil_usuario, name='perfil_usuario'),


    #Paths de plano de associacao
    path('cadastrar_plano/', planos_views.plano_associacao, name='cadastrar_plano'),
   




]

