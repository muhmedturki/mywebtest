from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('student', views.student, name='student.html'),
   # path('products', views.products, name='products.html'),
   # path('product', views.product, name='product.html'),
]