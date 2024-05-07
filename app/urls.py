from django.urls import path
from .views import ProductMobile, ProductDetail

urlpatterns = [
    path('', ProductMobile.as_view(), name="index"),
    path('detail/<slug:slug>/', ProductDetail.as_view(), name="detail")
]
