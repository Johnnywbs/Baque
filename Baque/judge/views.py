from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"",)

def criar_questao(request):
    '''if request.method == 'POST':
        # …
    else:'''
    return render(request,"",)

def questao(request):
    return render(request,"",)
