from django.urls import path
from . import views
urlpatterns = [
    path("categories/",views.CategoryListView.as_view(),name="category-list"),
    path("categories/<slug:slug>",views.CategoryDetailsView.as_view(),name="category-details"),
    path("products/",views.ProductListView.as_view(),name="product-list"),
    path("products/<slug:slug>",views.ProductDetailView.as_view(),name="product-detail"),
    path("categories/<slug:slug>/products/",views.CategoryProductView.as_view(),name="category-product-details")
]