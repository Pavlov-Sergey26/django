from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ['About site', 'Add post', 'Feedback', 'Come in']
menu2 = ['About site2', 'Add post2', 'Feedback2', 'Come in2']
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts':posts, 'menu':menu, 'title':'Main page'})

def about(request):
    return render(request, 'women/about.html', {'menu':menu2, 'title':'About site'})

def categories(request, categoriesid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{categoriesid}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Cтраница не найдена</h1>')