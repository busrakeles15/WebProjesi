from django.shortcuts import render,get_object_or_404
from .models import  IletisimModel

def iletiListe(request):
    iletiler = IletisimModel.objects.all()
    return render(request,"iletisim/liste.html",
    {"iletis":iletiler})

def iletiDetay(request,pk):
    ileti = get_object_or_404(IletisimModel,pk=pk)
    return render(request,"iletisim/detay.html",
    {"ileti":ileti})