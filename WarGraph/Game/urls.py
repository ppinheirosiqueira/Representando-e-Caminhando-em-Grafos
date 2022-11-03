from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jogo', views.jogo, name="jogo"),
    path('escolha/<str:nome>', views.escolha, name="escolha"),
    path('FimDeJogo', views.fim, name="fim"),
    path('reset', views.reset, name="reset")
]