from django.urls import include, re_path
from .views import usuario_views

urlpatterns = [
    re_path('login', usuario_views.login),
    re_path('cadastro', usuario_views.cadastro),
    re_path('teste_token', usuario_views.test_token),
    re_path('perfil', usuario_views.perfil),




]
