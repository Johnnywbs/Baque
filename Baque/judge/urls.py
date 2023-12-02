from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("problem_list/",views.problem_list,name="problem_list"),
    path("submission_list/",views.submission_list,name="submission_list"),
    path("create/",views.create,name="create"),
    path("problem/<int:id>",views.problem,name="problem"),
    path("submission/<int:id>",views.submission,name="submission"),
]
