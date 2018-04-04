from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import article, comment
from .forms import articleForm, commentForm

# Create your views here.


def index(request):
    articles_list = article.objects.all()
    context = {
        'articles_list': articles_list,
    }
    return render(request, 'testBlog/index.html', context)


def nuevo(request):
    if request.method == 'POST':
        form = articleForm(request.POST)

        if form.is_valid():
            new_article = form.save()
            messages.info(request, 'Articulo creado con exito')
            form = articleForm()
            return redirect(index)
    else:
        form = articleForm()
    return render(request, 'testBlog/nuevo.html', {'form': form, 'target':'/nuevo/'})

def ver(request, id):
    obj = article.objects.get(pk=id)
    com = list(comment.objects.filter(article=obj))
    context = {
        'obj': obj,
        'comments': com
    }
    return render(request, 'testBlog/ver.html', context)

def eliminar(request, id):
    obj = article.objects.get(pk=id)
    obj.delete()
    messages.info(request, 'Articulo eliminado con exito')
    return redirect(index)

def autor(request, id):
    obj = article.objects.get(pk=id)
    messages.info(request,obj.theAuthor())
    return redirect(index)

def comentario(request, id):
    if request.method == 'POST':
        form = commentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            art = article.objects.get(pk=id)
            new_comment.article = art
            new_comment.save()
            messages.info(request, 'Comentario creado con exito')
            return redirect(ver, id=id)

    else:
        form = commentForm()
    return render(request, 'testBlog/nuevo.html', {'form': form, 'target':'/comentario/'+str(id)})
