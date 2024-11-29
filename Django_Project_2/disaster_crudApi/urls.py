from django.urls import path
from .views import * 

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductRetrieveAPIView.as_view(), name='product-retrieve'), 
    path('products/create/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/<int:pk>/partial-update/', ProductPartialUpdateAPIView.as_view(), name='product-partial-update'),
    path('products/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
]
