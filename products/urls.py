from django.urls import path

from .views import (product_detail_view, product_create_view,
                    dynamic_lookup_view, product_delete_view, produce_list_view,)

app_name='products'
urlpatterns = [
    path('productindex/', produce_list_view, name='productlist'),
    path('product/', product_detail_view),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('create/', product_create_view),
]
