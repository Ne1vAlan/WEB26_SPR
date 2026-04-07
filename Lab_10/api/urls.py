from django.urls import path
from api.views import *

urlpatterns = [
    #PRODUCTS
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),

    #CATEGORIES
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),

    #CATEGORY PRODUCTS
    path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view()),
]