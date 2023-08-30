from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def index(request):
    categories_list = Categoria.objects.all()
    post_list = Post.objects.all()
    context = {'catgories_list': categories_list,
               'post_list':post_list}
    return render(request, 'index.html',context)

def cat_post(request, categoria_id):
    categories_list = Categoria.objects.all()
    category = get_object_or_404(Categoria, pk=categoria_id)
    return render(request, 'index.html',{'catgories_list':categories_list,'categoria':category})