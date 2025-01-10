from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from rent_house.forms import AddPostForm
from rent_house.models import Appartments
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView


class Index(ListView):
    model= Appartments
    template_name = 'rent_house/index.html'
    context_object_name = 'posts'
    paginate_by =3
    extra_context = {
        'title':'Главная страница',
    }

    def get_queryset(self):
        return Appartments.objects.filter(is_published=True).select_related('cat')

def about(request):
    return render(request,'rent_house/about.html',{'title':'О сайте'})


class ShowPost(DetailView):
    template_name = 'rent_house/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):#отображаем имя каждой записи
        context=super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        return context

    def get_object(self,queryset=None):#отображаем только опубликованные посты
        return get_object_or_404(Appartments.objects.filter(is_published=True),slug=self.kwargs[self.slug_url_kwarg])
        #слаг формируется на основе slug_url_kwarg

class add_apartment(CreateView):
    form_class = AddPostForm
    template_name = 'rent_house/add_apart.html'
    success_url= reverse_lazy('home')
    extra_context = {
        'title':'Добавить обьявление',
    }

class edit_page(UpdateView):
    model= Appartments
    fields= '__all__'
    template_name = 'rent_house/edit_page.html'
    success_url= reverse_lazy('home')
    extra_context = {
        'title':'Редактировать обьявление',
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