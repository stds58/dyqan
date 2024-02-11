from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView )
from django.urls import reverse_lazy
from .models import Product
from .forms import ImageForm, ProductForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

class ProductsList(ListView):
    model = Product
    qyeryset = Product.objects.filter(price__lt=300).order_by('data_create')
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 6
    #return render(request, 'spring_pot_app/index.html', context_dict)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'downloadimage.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'downloadimage.html', {'form': form})


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    #success_url = reverse_lazy('back to calling url') #reverse_lazy('product')


    def get_success_url(self):
        print(f"HTTP_REFERER-{self.request.META.get('HTTP_REFERER')}")
        return self.request.META.get('HTTP_REFERER')



