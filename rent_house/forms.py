from django import forms

from rent_house.models import Appartments, Category


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана',label='Категория')
    class Meta:
        model = Appartments
        fields = ['title','slug','description','photo','payment','number_of_rooms','size_of_apartment','floor','furniture','technique','cat','is_published']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'is_published':'Опубликовать','slug': 'URL'}
