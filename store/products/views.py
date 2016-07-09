from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def product_list(request):
	product = Product.objects.all()
	return render (request, 'products/index.html', {'product': product})