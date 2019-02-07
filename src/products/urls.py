from django.urls import path
from .views import ProductList, ProductDetailView


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
