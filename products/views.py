from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# /products -> index
# filter for filtering those above a certain amount or o/s, get for single product
# save for inserting a new one or updating an existing one


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New products')


def offers(request):
    return HttpResponse('20% off all products')

