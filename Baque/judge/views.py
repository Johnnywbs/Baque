from django.shortcuts import render, redirect
from .models import Problem
from .forms import ProblemForm

def create(request):
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save()
            return redirect('problem', problem.id)
    form = ProblemForm()
    return render(request,"judge/create.html", {'form':form})

def problem(request, id):
    p = Problem.objects.get(pk=id)
    return render(request,"judge/problem.html", {'problem' : p})
