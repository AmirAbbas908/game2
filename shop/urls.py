from django.contrib import admin
from django.urls import path
from .views import IndexView,ProductDetailView
app_name='shop'
urlpatterns = [
path('home/',IndexView.as_view(),name='home'),
path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]