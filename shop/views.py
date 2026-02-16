from django.shortcuts import render
from .models import Product
# Create your views here.
def index_view(request):
    context = {
        'popular_games':Product.objects.all()
    }
    return render(request,"index.html",context)