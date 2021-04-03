from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.
class BaseView(View):
    views={}


class HomeView(BaseView):
    def get(self,request):
        self.views['categories']=Category.objects.filter(status='active')
        self.views['sliders']=Slider.objects.filter(status='active')
        self.views['brands']=Brand.objects.filter(status='active')
        self.views['ads']=Ad.objects.all()
        self.views['hots']=Item.objects.filter(label='hot')
        self.views['news']=Item.objects.filter(label='new')
        self.views['sales']=Item.objects.filter(label='sale')
        self.views['defaults']=Item.objects.filter(label='')
        self.views['feedbacks']=Feedback.objects.filter(status ='active')
        


        return render(request,'index.html',self.views)

class ItemDetailView(BaseView):
    def get(self,request,slug):
        self.views['item_detail'] = Item.objects.filter(slug = slug)
        self.views['brand'] = Brand.objects.filter(status="active")
        self.views['count'] = []
        for i in self.views['brand']:
            count_food= Item.objects.filter(brand = i.id).count()
            d={'name': i.name,'count': count_food}
            self.views['count'].append(d)

        self.views['count_cat'] = Category.objects.filter(status="active")
        self.views['cat_count'] = []
        for i in self.views['count_cat']:
            count_food= Item.objects.filter(category = i.id).count()
            d={'name': i.name,'image':i.image,'cat_count': count_food}
            self.views['cat_count'].append(d)
            

        cat=Item.objects.get(slug=slug).category_id
        self.views['catitems']=Item.objects.filter(category = cat)
        return render(request,'product-detail.html',self.views)

class CheckoutView(BaseView):
    def get(self,request):
        return render(request,'checkout.html')

class ContactView(BaseView):
    def get(self,request):
        return render(request,'contact.html')

class LoginView(BaseView):
    def get(self,request):
        return render(request,'login.html')

class MyAccountView(BaseView):
    def get(self,request):
        return render(request,'my-account.html')



class ProductListView(BaseView):
    def get(self,request):
        self.views['items']=Item.objects.filter(status="active")
        return render(request,'product-list.html',self.views)

class WishListView(BaseView):
    def get(self,request):
        return render(request,'wishlist.html')

class CategoryView(BaseView):
    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id # get takes just one value when placed with .id # filter takes multiple value
        self.views['catdetail'] = Item.objects.filter(category = cat_id)
        return render(request,'product-list.html',self.views)
