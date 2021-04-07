from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
     path('',HomeView.as_view(),name='home'),
     path('products/<slug>',ItemDetailView.as_view(),name='products'),  # the slug value comes from model
     path('category/<slug>',CategoryView.as_view(),name='category'),
     path('search',SearchView.as_view(),name='search'),
     # path('checkout',CheckoutView.as_view(),name='checkout'),
     path('contact',contact,name='contact'),
     path('account',signup,name='account'),
     # path('account',signup,name='account'),
     # path('login',LoginView.as_view(),name='login'),
     # path('my-account',MyAccountView.as_view(),name='my-account'),
     
     path('product-list',ProductListView.as_view(),name='productlist'),
]