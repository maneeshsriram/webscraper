from django.urls import path
from . import views

urlpatterns = [
    path('ebay', views.ebay, name='ebay'),
    path('flipkart', views.flipkart, name='flipkart'),
    path('gimages', views.gimages, name='gimages'),
]
