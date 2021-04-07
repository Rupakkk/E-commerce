from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
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
    def get(self,request,slug): # this slug is the value passed from url
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

# class CheckoutView(BaseView):
#     def get(self,request):
#         return render(request,'checkout.html')



# class LoginView(BaseView):
#     def get(self,request):
#         return render(request,'login.html')

# class MyAccountView(BaseView):
#     def get(self,request):
#         return render(request,'my-account.html')



class ProductListView(BaseView):
    def get(self,request):
        self.views['items']=Item.objects.filter(status="active")
        return render(request,'product-list.html',self.views)

# class WishListView(BaseView):
#     def get(self,request):
#         return render(request,'wishlist.html')

class CategoryView(BaseView):
    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id # get takes just one value when placed with .id # filter takes multiple value
        self.views['catdetail'] = Item.objects.filter(category = cat_id)
        return render(request,'product-detail.html',self.views)


class SearchView(BaseView):
    def get(self,request):
        # query = request.GET['search',None]
        if request.method == 'GET':
            query = request.GET['search']
            self.views['search_product'] = Item.objects.filter(description__icontains = query) #  icontains check for the search value within the Item
            return render(request,'search.html',self.views)

        return render(request,'search.html')

def contact(request):
    if request.method == "POST":
        Name=request.POST['name']
        Email=request.POST['email']
        Subject=request.POST['subject']
        Message=request.POST['message']
        data=Contact.objects.create(
            name = Name,
            email = Email,
            subject = Subject,
            message = Message
        )
        data.save()
        messages.success(request,'The form is Submitted')
        return render(request,'contact.html',views)

    return render(request,'contact.html')


def signup(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        Password = request.POST['password']
        Cpassword = request.POST['cpassword']
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        if Password==Cpassword:
            if User.objects.filter(username = Username).exists():
                messages.error(request,'This username is already taken')
                return redirect('home:account')
            elif User.objects.filter(email = Email).exists():
                messages.error(request,'This email is already taken')
                return redirect('home:account')
            else:
                user = User.objects.create_user(
                    username = Username,
                    email = Email,
                    password = Password,
                    first_name = Fname,
                    last_name = Lname
                )
                user.save()
                messages.success(request,'You are registered')
                return redirect('/')

        else:
            messages.error(request,'These passwords do not match')
            return redirect('home:account')

    return render(request,'signup.html')


# def review(request):
#     if request.method == "POST":
#         Name=request.POST['name']
#         Email=request.POST['email']
#         Subject=request.POST['subject']
#         Message=request.POST['message']
#         data=Contact.objects.create(
#             name = Name,
#             email = Email,
#             subject = Subject,
#             message = Message
#         )
#         data.save()
#         messages.success(request,'The form is Submitted')
#         return render(request,'contact.html',views)

#     return render(request,'contact.html')