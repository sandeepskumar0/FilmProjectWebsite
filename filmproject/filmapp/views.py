from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import  Film
from . forms import FilmForm
# Create your views here.
def index(request):
        film = Film.objects.all()
        context = {
            'film_list':film
        }
        return render(request, 'index.html', context)
def detail(request,film_id):
    film=Film.objects.get(id=film_id)
    return render(request,"detail.html",{'film':film})
def add_film(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        imgs = request.FILES['imgs']
        film=Film(name=name,desc=desc,year=year,imgs=imgs)
        film.save()


    return render(request,'add.html')

def update(request,id):
    film=Film.objects.get(id=id)
    form=FilmForm(request.POST or None,request.FILES,instance=film)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'film':film})
def delete(request,id):
    if request.method=='POST':
        film=Film.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(request,'delete.html')