from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from rent_house.forms import AddPostForm
from rent_house.models import Appartments
from django.views.generic import TemplateView,ListView,CreateView,DetailView


class Index(ListView):
    model= Appartments
    template_name = 'rent_house/index.html'
    context_object_name = 'posts'
    extra_context = {
        'title':'Главная страница',
    }

    def get_queryset(self):
        return Appartments.objects.filter(is_published=True).select_related('cat')


# def index(request):
#     posts=Appartments.objects.filter(is_published=True)
#     data = {
#         'title':'Главная страница',
#         'posts':posts,
#     }
#     return render(request,'rent_house/index.html',context=data)

def about(request):
    return render(request,'rent_house/about.html',{'title':'О сайте'})



def show_post(request, post_slug):
    post = get_object_or_404(Appartments, slug=post_slug)
    data = {
        'title': post.title,
        'post': post,
    }
    return render(request, 'rent_house/post.html', data)



# def add_apartment(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     data = {
#         'title': 'Добавление статьи',
#         'form': form
#     }
#     return render(request, 'rent_house/add_apart.html', data)

class add_apartment(CreateView):
    model = Appartments
    fields = '__all__'
    template_name = 'rent_house/add_apart.html'
    extra_context = {
        'title':'Добавить обьявление',
    }


def login(request):
    pass

def logout(request):
    pass

def register(request):
    pass

def contact(request):
    return render(request,'rent_house/contact.html')

def profile(request):
    return render(request,'rent_house/profile.html')