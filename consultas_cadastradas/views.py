from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def battles(request):
    return render(request, 'html/battles.html')

def item(request):
    return render(request, 'html/item.html')

def Lumiose(request):
    return render(request, 'html/lumiose.html')

def Pokemon(request):
    return render(request, 'html/pokemon.html')

def dlc(request):
    return render(request, 'html/dlc.html')