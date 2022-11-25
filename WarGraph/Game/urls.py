from django.urls import path

from . import views

"""
Aqui são colocadas as URL's utilizadas pelo aplicativo Game para decidir quais funções são chamadas em cada URL do jogo.
As funções no Views retornam algum render, que determina o HTML que será utilizado e mostrado ao jogador.
"""

urlpatterns = [
    path('', views.index, name="index"),
    path('start', views.start, name="start"),
    path('jogo', views.jogo, name="jogo"),
    path('escolha/<str:nome>', views.escolha, name="escolha"),
    path('dificuldade', views.dificuldade, name="dificuldade"),
    path('dificuldade/<str:escolha>', views.esc_dificuldade, name="escolha_dificuldade"),
    path('cidade', views.cidade, name="cidade"),
    path('cidade/<str:escolha>', views.esc_cidade, name="escolha_cidade"),
    path('FimDeJogo', views.fim, name="fim"),
    path('reset', views.reset, name="reset"),
    path('about', views.about, name="about")
]