from django.shortcuts import render
from .models import  IletisimModel

def iletiListe(request):
    iletiler = IletisimModel.objects.all()
    return render(request,"iletisim/liste.html",
    {"iletis":iletiler})