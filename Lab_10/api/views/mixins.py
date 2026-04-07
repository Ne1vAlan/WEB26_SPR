from rest_framework import mixins, generics

from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer

#PRODUCTS LIST

class ProductListAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

#PRODUCT DETAIL

class ProductDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get(self, request, product_id):
        return self.retrieve(request, product_id=product_id)

    def put(self, request, product_id):
        return self.update(request, product_id=product_id)

    def delete(self, request, product_id):
        return self.destroy(request, product_id=product_id)

#CATEGORIES

class CategoryListAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'

    def get(self, request, category_id):
        return self.retrieve(request, category_id=category_id)

    def put(self, request, category_id):
        return self.update(request, category_id=category_id)

    def delete(self, request, category_id):
        return self.destroy(request, category_id=category_id)

#PRODUCTS BY CATEGORY

class CategoryProductsAPIView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)

    def get(self, request, category_id):
        return self.list(request)