from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    ItemDetailView,
    checkout,
    HomeView
)

app_name = 'market'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<slug:slug>/', views.ItemDetailView.as_view(), name='product'),
]

