from django.shortcuts import render
from django.http import HttpResponse
import json
from . import monTicTac
import time

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def game(request):
    order = [i for i in range(12)]
    return render(request, 'game.html',{"order":order})

def psutil(request):
    #person = json.loads( personString ) 
    data= json.loads(request.GET.getlist('data')[0])

    #recher qui a commencer True si c'est l'utilsateur et false si non
    reponse=False
    i=0
    for l in data["matrice"]:
        if "O" in l:
            reponse=True
        if "O" in l or "X" in l:
            i+=1

    if reponse==False and i>1:
        reponse = True

    Start = time.time()
    reponseRequest = monTicTac.fin(data["matrice"], reponse,data["numeroChoisi"])
    ch = 1
    for i in range(len(data["matrice"][0])):
        for j in range(len(data["matrice"][0])):
            if (i,j) == reponseRequest:
                print("temp joue==",time.time()-Start)
                return HttpResponse(str(ch))
            ch+=1
    
    
    return HttpResponse("j'ai rien trouver")