from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("criar_questao/",views.criar_questao,name="criar_questao"),
    path("questao/",views.questao,name="questao")
]
