from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search'),
]