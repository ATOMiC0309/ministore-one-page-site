from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Product


# Create your views here.

class ProductMobile(ListView):
    model = Category
    template_name = "app/index.html"
    context_object_name = "categories"


class ProductDetail(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "app/detail.html"
