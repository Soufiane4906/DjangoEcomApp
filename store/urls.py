from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', homePage, name='home'),
    path('products', productsView, name='products'),
    path('about', aboutView, name='about'),
    path('checkout', checkOutView, name='checkout'),
    path('blog', blogView, name='blog'),
    path('detail/<slug:slug>', productDetail, name='detail'),
    path('checkout', checkOutView, name='checkout'),
    path('addtocart/<int:pk>', addCart, name='addtocart'),
    path('decrease/<int:pk>', decreaseQuantity, name='decrease'),
    path('remove/<int:pk>', removeCartItem, name='remove'),
    path('logout', logoutUser, name='logout'),
    path('404', pageNotFound, name='404'),
    path('contact', contact, name='contact'),
    path('blogDetail/<slug:slug>', blogDetail, name='blogDetail'),



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
