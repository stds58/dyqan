from django import forms
from .models import Product


class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'tekst','price','vnalicii','image','category')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'tekst', 'price', 'vnalicii', 'image', 'category']
        labels = {
            'title': 'название',
            'tekst': 'описание',
            'price': 'цена',
            'vnalicii': 'в наличии',
            'image': 'картинка',
            'category': 'категория'
        }
        widgets = {
            'image': forms.FileInput(),
        }

