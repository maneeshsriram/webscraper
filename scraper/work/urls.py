from django.urls import path
from . import views

urlpatterns = [
    path('ebay', views.ebay, name='ebay'),
    path('Jebay', views.Jebay, name='Jebay'),
    path('flipkart', views.flipkart, name='flipkart'),
    path('Jflipkart', views.Jflipkart, name='Jflipkart'),
    path('twitter', views.twitter, name='twitter'),
    path('Jtwitter', views.Jtwitter, name='Jtwitter'),
    path('flipkartReview', views.flipkartReview, name='flipkartReview'),
    path('JflipkartReview', views.JflipkartReview, name='JflipkartReview'),
    path('gimages', views.gimages, name='gimages'),
    path('smart', views.smart, name='smart'),
]
