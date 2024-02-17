from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    namecat = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.namecat}'


class Product(models.Model):
    title = models.CharField(max_length=20)
    tekst = models.TextField()
    price = models.FloatField(default = 0.0)
    data_create = models.DateTimeField(auto_now_add = True)
    vnalicii = models.BooleanField()
    image = models.ImageField(null = True, upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
#https://habr.com/ru/articles/763528/ компрес картинки
#https://django.fun/qa/372489/
#Django crispy forms
    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f'{self.title}'
        #return u'<img src="%s"/>' % self.image.url
        #return f'{self.title} <img src="http://127.0.0.1:8000{self.image.url}" width="50" />'

    def get_absolute_url(self):
        return reverse('product_number', args=[str(self.id)])


class Klient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='Subscribe')

    def __str__(self):
        return f'{self.user}'


class Subscribe(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.klient} {self.product}'

class IstoriaSubscribe(models.Model):
    title = models.CharField(max_length=20)
    tekst = models.TextField()
    data = models.DateTimeField(auto_now_add = True)
    subscribe = models.ForeignKey(Subscribe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title } {self.data} {self.subscribe}'


class Zakaz(models.Model):
    summa = models.FloatField(default = 0.0)
    data_create = models.DateTimeField(auto_now_add = True)
    oplaceno = models.BooleanField(default = False)
    data_oplati = models.DateTimeField(blank = True, null = True)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='Korzina')

    def get_summa (self):
        summa_current = 0
        ids = Zakaz.objects.filter(klient = self.klient, oplaceno=False).values('id')
        if len(ids) == 1:
            korzina_current = Korzina.objects.filter(zakaz = ids[0]['id']).values('product')
            for id in korzina_current:
                price = Product.objects.filter(id = id['product']).values('price')
                summa_current += price[0]['price']
        self.summa = summa_current
        self.save()

        # python manage.py shell
        # from bazaapp.models import *
        #a1 = Klient.objects.filter(id=2).first()
        #z1 = Zakaz.objects.create(klient=a1)
        #p1 = Product.objects.filter(id=1).first()
        #p2 = Product.objects.filter(id=2).first()
        #kor1 = Korzina.objects.create(zakaz=z1,product=p1)
        #kor2 = Korzina.objects.create(zakaz=z1,product=p2)
        #z1.get_summa()

    def __str__(self):
        return f'{self.klient} {self.product} {self.data_create}'


class Korzina(models.Model):
    zakaz = models.ForeignKey(Zakaz, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.zakaz } {self.product}'




