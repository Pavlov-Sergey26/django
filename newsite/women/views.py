from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse('Страница приложения women')

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