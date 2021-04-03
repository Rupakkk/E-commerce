from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
     path('',HomeView.as_view(),name='home'),
     path('products/<slug>',ItemDetailView.as_view(),name='products'),
     path('category/<slug>',CategoryView.as_view(),name='category'),
     # path('cart',CartView.as_view(),name='cart'),
     path('checkout',CheckoutView.as_view(),name='checkout'),
     path('contact',ContactView.as_view(),name='contact'),
     path('login',LoginView.as_view(),name='login'),
     path('my-account',MyAccountView.as_view(),name='my-account'),
     
     path('wishlist',WishListView.as_view(),name='wishlist'),
]