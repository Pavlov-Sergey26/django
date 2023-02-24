from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title':'About Site', 'url_name':'about'},
        {'title':'Add post', 'url_name':'add_page'},
        {'title':'Feedback', 'url_name':'contact'},
        {'title':'Come in', 'url_name':'login'}]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {'posts':posts, 
                'menu':menu, 
                'cats':cats,
                'title':'Main page',
                'cat_selected':0
                }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu':menu, 'title':'About site'})

def add_page(request):
    return HttpResponse(f'Добавление страницы')


def contact(request):
    return HttpResponse(f'Обратная связь')

def login(request):
    return HttpResponse(f'Авторизация')

def show_post(request, post_id):
    return HttpResponse(f"Отображения статьи с id={post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
        
    context = {'posts':posts, 
                'menu':menu, 
                'cats':cats,
                'title':'Display category',
                'cat_selected':cat_id
                }
    return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Cтраница не найдена</h1>')