from django.shortcuts import render,get_object_or_404,redirect
from .models import  IletisimModel
from .forms import  IletisimForm

def iletiListe(request):
    iletiler = IletisimModel.objects.all()
    return render(request,"iletisim/liste.html",
    {"iletis":iletiler})

def iletiDetay(request,pk):
    ileti = get_object_or_404(IletisimModel,pk=pk)
    return render(request,"iletisim/detay.html",
    {"ileti":ileti})


def yeni_ileti(request):
    if request.method == "POST":
        form = IletisimForm(request.POST)
        if form.is_valid():
            ileti = form.save(commit=False)
            #######################
            ileti.save()
            return redirect('iletiDetay',pk=ileti.pk)
    else:
        form = IletisimForm()
    return render(request,"iletisim/duzenle.html",{"form":form})

def iletiduzenle(request,pk):
    ileti = get_object_or_404(IletisimModel,pk=pk)
    if request.method == "POST":
        form = IletisimForm(request.POST,instance=ileti)
        if form.is_valid():
            ileti = form.save(commit=False)
            #######################
            ileti.save()
            return redirect('iletiDetay',pk=ileti.pk)
    else:
        form = IletisimForm(instance=ileti)
    return render(request,"iletisim/duzenle.html",{"form":form})