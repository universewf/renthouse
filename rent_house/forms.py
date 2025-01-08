from django import forms

from rent_house.models import Appartments, Category

class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категории")
    class Meta:
        model = Appartments
        fields = ['title','slug','description','photo','payment','number_of_rooms','size_of_apartment','floor','furniture','technique','cat','is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 3}),
        }
        labels = {'slug': 'URL','is_published':'Опубликовать'}