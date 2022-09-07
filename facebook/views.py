
#from multiprocessing import reduction
#import re
from os import remove
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*

from django.contrib.auth.hashers import check_password,make_password

# Create your views here.py
def index(request):
    if request.method=="POST":
        product_id = request.POST.get("cartid")
        remove=request.POST.get('minus') 
        cart_dict = request.session.get('cart')
        print(cart_dict)
        if cart_dict:
            quantity = cart_dict.get(product_id)
            if quantity:
                if remove:
                    if quantity <=1 :
                        cart_dict.pop(product_id)
                        
                    else:
                        cart_dict[product_id]=quantity-1
                else:
                    cart_dict[product_id]=quantity+1
            else:
                cart_dict[product_id]=1

        else:
         cart_dict={}
         cart_dict[product_id]= 1
        request.session['cart']=cart_dict
        print(request.session['cart'])
    
   
 
    cate = Category.objects.all()
    c={}
    for i in cate:
        c.update({i.id:i.name})
        request.session['cate_name'] = c
    category_id=request.GET.get('cate_id')
 
    if 'search' in request.GET:     
        search = request.GET['search']
        try:
            categ= Category.objects.get(name=search)
            if categ:
                 products=product.objects.filter(Category=categ.id)
        except:
             products=product.objects.filter(product_name__icontains=search)

       # products = product.objects.filter(product_name__icontains=search)   
          
    elif  category_id:
        products=product.objects.filter(Category=category_id)
    else:
        products=product.objects.all()
    return render(request,'home.html',{'cat':cate,'pro':products})


def signup(request):
    if request.method =="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email_id = request.POST.get('email')
        password = request.POST.get('psd')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        user_info = registration(first_name=fname,last_name=lname, 
        email=email_id,mobile_no=mobile,gender=gender,password = make_password(password))
        user_info.save()


    return HttpResponse("success")

def login(request):
    if request.method=="POST":
      error_msg = None
      emailid = request.POST.get('email')
      password = request.POST.get('psd')
    try:
    

        fetch_info = registration.objects.get(email=emailid)
        if check_password(password,fetch_info.password):
            
            request.session['fname']=fetch_info.first_name
            request.session['customer_id']=fetch_info.id
            request.session['email']=fetch_info.email
            return redirect('home')
        else:
            error_msg = "PASSWORD IS INCORRECT"
    except:
            error_msg = "EMAIL IS INCORRECT"                     

    return render(request,'home.html',{'error':error_msg})
    


def logout(request):
     request.session.clear()
     return redirect('home')
    
        
def cart_info(request):

    cart_items=request.session.get('cart').keys()
    filtered_product=product.objects.filter(id__in=list(cart_items))
    return render(request,'cart.html',{'filtered_product':filtered_product})


def checkout(request):
    if request.method =="POST":
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        customerid=request.session.get('customer_id')
        cart=request.session.get('cart')
        product_id= product.objects.filter(id__in=list(cart.keys()))
        if not customerid:  
              
            return HttpResponse('plz login')
        for pro in product_id:
            save_order_dtls=order (address=address,
            mobile_no = mobile, 
            product_id=pro,
            customer=registration(id=customerid),
            quantity=cart.get(str(pro.id)),
            price=pro.price) 
 
            save_order_dtls.save() 
            request.session['cart']={}     
            return redirect("cartdtls")