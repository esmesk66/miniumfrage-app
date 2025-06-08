from django.shortcuts import render, redirect
from .models import Stimme

def stimmen(request):
    if request.method == "POST":
        fach = request.POST.get("fach")
        if fach:
            Stimme.objects.create(fach=fach)
            return redirect('/umfrage/')
    fächer = ['Mathe', 'Informatik', 'Deutsch', 'Englisch']
    stimmen = Stimme.objects.all()
    return render(request, 'umfrage/umfrage.html', {'fächer': fächer, 'stimmen': stimmen})
