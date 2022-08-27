from django.urls import path, re_path

from products import views

urlpatterns = [
    path("add_product/", views.add_product, name="add_product"),
    path("add_combination/", views.add_combination, name="add_combination"),
    path("detail/<product_sku>/", views.product_detail, name="product_detail"),
    re_path(r"^(page/(?P<page>\d+))?/$/", views.all_products, name="products"),
    path(r"", views.all_products, name="products"),
]
