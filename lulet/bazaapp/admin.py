from django.contrib import admin
from .models import Category, Product, Klient, Subscribe, Zakaz, Korzina


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Klient)
admin.site.register(Subscribe)
admin.site.register(Zakaz)
admin.site.register(Korzina)

