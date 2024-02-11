from django.urls import path
from .views import ProductsList, ProductDetail, image_upload_view, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
   path('catalog/', ProductsList.as_view(), name='product'),
   path('catalog/<int:pk>/', ProductDetail.as_view(), name='product_number'),
   path('upload/', image_upload_view),
   path('manage/create/', ProductCreate.as_view(), name= 'product_create'),
   path('manage/update/<int:pk>/', ProductUpdate.as_view(), name= 'product_update'),
   path('manage/delete/<int:pk>/', ProductDelete.as_view(), name= 'product_delete'),
]