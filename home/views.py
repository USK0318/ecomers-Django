from django.shortcuts import render
from django.http import HttpResponse
from .forms import productform,registerform,editform
from .models import user_info,Product,cart,order
from django.contrib import messages
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required ,user_passes_test
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .models import Product, cart
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import order
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required(login_url='login')
def home(request):
    a=Product.objects.all()
    return render(request, 'home.html',{'data':a})

@login_required(login_url='login')
def shop(request):
    a=Product.objects.all()
    return render(request, 'shop.html',{'data':a})

@login_required(login_url='login')
def about(request):
    a=Product.objects.all()
    print(a)
    return render(request, 'about.html', {'data':a})    

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        # Retrieve the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Validate the data (you can customize this as needed)
        if not name or not email or not message:
            messages.error(request, 'All fields are required.')
            return redirect('contact')
        
        # Construct the email message including the user's email in the message body
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        # Try to send the email
        try:
            send_mail(
                subject=f"New message from {name}",
                message=email_message,
                from_email='yourfixedemail@domain.com',  # Your fixed email address
                recipient_list=['uppalapatisaikiran27@gmail.com'],  # Your email
                fail_silently=False,
            )
            # If email was sent successfully
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
        except Exception as e:
            # Log the exception or handle it in a way that's suitable for your application
            print(f"Error sending email: {e}")  # Consider using Python's logging module for better logging in production
            messages.error(request, 'There was an error sending your message.')
            return redirect('contact')
    
    # Render the contact form template
    return render(request, 'contact.html')


def login_fun(request):
    if request.method=='POST':
        a=request.POST['User']
        b=request.POST['password']
        v=authenticate(request,username=a,password=b)
        if v==None:
            messages.error(request,'Invalied USER or PASSWORD')
            return render(request,'login.html')
        else:
            login(request,v)
            return redirect('home')
    return render(request,'login.html')

def register(request):
    a=registerform()
    if request.method=='POST':
        x=registerform(request.POST)
        print(x)
        if x.is_valid()==True:
            x.save()
            return redirect('login')
        else:
            messages.error(request,'user not created')
            return render(request,'register.html',{'form':x})
    return render(request, 'register.html', {'form':a})

@login_required(login_url='login')
def logout_fun(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def user(request):
    a=User.objects.get(id=request.user.id)
    try:
        b=user_info.objects.get(user_id=request.user.id)
        data = {'id':a,'email':a.email,'first_name':a.first_name,'last_name':a.last_name ,'is_staf':a.is_staff}
        return render(request, 'user.html',{'i':data,'j':b})
    except:
        return render(request, 'user.html',{'i':a})

@user_passes_test(lambda u: u.is_staff)
@login_required(login_url='login')
def upload(request):
    a=productform()
    if request.method=="POST":
        b=productform(request.POST,request.FILES)
        if b.is_valid()==True:
            x=b.save( commit=False)
            x.user_id=request.user.id
            x.save()
            messages.success(request,'Data saved')
            return render(request,'form.html',{'form':a})
        else:
            messages.error(request,'Data NOT saved')
            return render(request,'form.html',{'form':b})
    return render(request,'form.html',{'form':a})


@login_required(login_url='login')
def edit(request):
    if request.method == 'POST':
        form = editform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.id
            instance.save()
            return redirect('user')
        else:
            messages.error(request, 'Data not Saved')
            return render(request, 'edit.html', {'form': form})
    else:
        form = editform()
        return render(request, 'edit.html', {'form': form})

@login_required(login_url='login')
def addtocart(request, ids):
    cart.objects.create(user_id=request.user.id, product_id=ids)
    return redirect('shop')

@login_required(login_url='login')
def addorder(request, ids):
    a=Product.objects.get(product_id=ids)
    order.objects.create(user_id=request.user.id, product_id=ids,price=a.price)
    return redirect('shop')

@login_required(login_url='login')
def deletecart(request, ids):
    cart.objects.filter(product_id=ids).delete()
    return redirect('cart')

@login_required(login_url='login')
def cart_info(request):
    items=[]
    user_cart = cart.objects.filter(user_id=request.user.id)
    for i in user_cart:
        items.append(i.product_id)

    all_products = Product.objects.all()
    products_in_cart = all_products.filter(product_id__in=items)
    return render(request, 'cart.html', {'data': products_in_cart})

from .models import order


@login_required(login_url='login')
def order_info(request):
    items = []
    user_orders = order.objects.filter(user_id=request.user.id)
    for i in user_orders:
        items.append(i.product_id)

    all_products = Product.objects.all()
    products_in_order = all_products.filter(product_id__in=items)
    return render(request, 'order.html', {'data': products_in_order})


@login_required(login_url='login')
def deleteorder(request, ids):
    order.objects.filter(product_id=ids).delete()
    return redirect('order')

@user_passes_test(lambda u: u.is_staff)
@login_required(login_url='login')
def viewpro(request):
    a=Product.objects.filter(user_id=request.user.id)
    return render(request, 'viewpro.html', {'data': a})

@user_passes_test(lambda u: u.is_staff)
@login_required(login_url='login')
def dashboard(request):
    a=Product.objects.filter(user_id=request.user.id)
    product_count = a.count()
    c=0
    for i in a:
        c=c+i.price
    return render(request, 'dashboard.html', {'product_count': product_count, 'total_price': c,'username':request.user.username})

from django.core.files.storage import default_storage

@user_passes_test(lambda u: u.is_staff)
@login_required(login_url='login')
def deletepro(request, ids):
    try:
        product = Product.objects.get(product_id=ids)
    except Product.DoesNotExist:
        # Handle case where product doesn't exist
        return HttpResponse("Product not found.", status=404)

    # Get the image associated with the product and delete it from storage
    if product.image:
        image_path = product.image.path
        default_storage.delete(image_path)

    # Delete the product instance
    product.delete()

    return redirect('viewpro')


@user_passes_test(lambda u: u.is_staff)
@login_required(login_url='login')
def editpro(request, ids):
    # Get the product instance you want to edit
    product_instance = get_object_or_404(Product, product_id=ids)
    
    if request.method == 'POST':
        # Pass instance to form to create a bounded form
        form = productform(request.POST, request.FILES, instance=product_instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.id
            instance.product_id = ids
            instance.save()
            return redirect('viewpro')
        else:
            messages.error(request, 'Data not Saved')
            return render(request, 'form.html', {'form': form})
    else:
        # Pass instance to form to create a bounded form
        form = productform(instance=product_instance)
        return render(request, 'form.html', {'form': form})
