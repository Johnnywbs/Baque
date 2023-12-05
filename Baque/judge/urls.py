from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("problem_list/",views.problem_list,name="problem_list"),
    path("submission_list/",views.submission_list,name="submission_list"),
    path("edit/",views.edit,name="edit"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("problem/<int:id>",views.problem,name="problem"),
    path("add_generator/<int:id>",views.add_generator,name="add_generator"),
    path("submission/<int:id>",views.submission,name="submission"),
]
