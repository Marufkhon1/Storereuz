from django.urls import path

from .views import *

urlpatterns = [
    path("", clothes_view, name="clothes_list"),
    path("add_product/", AddClothesView.as_view(), name="clothes_add"),
    path("update_product/<int:pk>", ClothesUpdateView.as_view(), name="update_product"),
    path("product_details/<int:pk>", ClothesDetailsView.as_view(), name="clothes_details"),
    path("delete_product/<int:clothes_id>", delete_product, name="delete_product"),
    path('add_to_cart/<int:clothes_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:clothes_id>/', remove_from_cart, name='remove_from_cart'),

]