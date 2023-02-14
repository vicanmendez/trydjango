from django.urls import path

from .views import(
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view,
    render_initial_data,
    dynamic_lookup_view)

app_name = 'products'

urlpatterns = [
    path("<int:id>/", dynamic_lookup_view, name='product-lookup'),
    path("<int:id>/delete/", product_delete_view, name='product-delete'),
    path("list/", product_list_view, name='product-list'),
    path("create/", render_initial_data, name='create'),
    path("detail/", product_detail_view, name='product-detail'),
    
]