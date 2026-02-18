from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Product



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_games'] = Product.objects.all()
        context['most_played'] = Product.objects.order_by('-play_count')[:6]
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product-details.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.play_count += 1
        obj.save()
        return obj


    
    
