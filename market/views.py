from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.template.response import TemplateResponse
from .models import Item, OrderItem, Order
# Create your views here.

def checkout(request):
    return render(request, "pages/checkout.html")


class HomeView(ListView):
    model = Item
    template_name = "pages/home.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "pages/product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item)
    order_item = OrderItem.objects.create(item=item)
