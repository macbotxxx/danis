from django.shortcuts import render, redirect
from .models import Product, Customer, Order
from django.forms import inlineformset_factory
from .forms import OrderFrom, CreateUserForm, CustomUser
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
from django.contrib.auth.models import Group



@unauthenticated_user
def register(request):
      form = CreateUserForm() 
      if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                  form.save()
                  username = form.cleaned_data.get('username')
                  messages.success(request, username + ' Your account have been created ') 
                  return redirect('login')
      context = {
            'form': form
      }
      return render(request, 'register.html', context)


@unauthenticated_user
def loginUser(request): 
      if request.method == "POST":
            username =  request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password= password)
            if user is not None:
                  login(request, user)
                  return redirect('home')
            else:
                  messages.info(request, 'Username or Password is incorrect')
      return render(request, 'login.html', {})

def logoutUser(request):
      logout(request)
      return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
      order = Order.objects.all()
      total_order = order.count()
      products = Product.objects.all()
      customers = Customer.objects.all()
      total_customer = customers.count()
      delivered = order.filter(status='Delivered').count()
      pending = order.filter(status="Pending").count()
      context = {
            'delivered': delivered,
            'pending': pending,
            'total_order': total_order,
            'total_customer': total_customer,
            'order': order,
            'customers': customers,
            'products': products
      }
      return render(request,'index.html', context)


@login_required(login_url='login')
@admin_only
def customer(request, pk_text):
      customers = Customer.objects.get(id=pk_text)
      order = customers.order_set.all()
      total_order = order.count()
      myFilter = OrderFilter(request.GET, queryset=order)
      order = myFilter.qs
      context = {
            'total_order': total_order,
            'order': order, 
            'customers': customers,
            'myFilter': myFilter,
      }
      return render(request,'customer.html', context)

def products(request):
      return render(request,'products.html', {})


@login_required(login_url='login')
def settings(request):
      user = request.user.customer
      form = CustomUser(instance=user)
      if request.method == "POST":
            form = CustomUser(request.POST,request.FILES, instance=user)
            if form.is_valid():
                  form.save()
      context = {
            'form': form
      }
      return render(request,'settings.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles = ['customer'])
def user(request):  
      order = request.user.customer.order_set.all()
      total_order = order.count()
      delivered = order.filter(status='Delivered').count()
      pending = order.filter(status='Pending').count()
      context = {
            'pending':pending,
            'delivered': delivered,
            'total_order':total_order,
            'order': order
      }
      return render(request,'user.html', context)


@login_required(login_url='login')
@admin_only
def createOrder(request, pk):
      OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra=10)
      customer = Customer.objects.get(id=pk)
      formset = OrderFormSet(instance=customer)
      form = OrderFrom(initial={'customer':customer})
      if request.method == 'POST':
            form = OrderFrom(request.POST)
            if form.is_valid:
                  form.save()
                  return redirect('/')
                  
      context = {
            'form': form
      }
      return render(request,'order_form.html', context)



@login_required(login_url='login')
@admin_only
def updateOrder(request, pk):
      order = Order.objects.get(id=pk)
      form = OrderFrom(instance=order)
      if request.method == 'POST':
            form = OrderFrom(request.POST, instance=order)
            if form.is_valid:
                  form.save()
                  return redirect('/')
      context = {
            'form': form
      }
      return render(request,'edit_order.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles = ['customer'])
def deleteOrder(request, pk):
      item = Order.objects.get(id=pk)
      if request.method == "POST":
            item.delete()
            return redirect('/')
      context = {
            'item': item
      }
      return render(request, 'delete.html', context)


   

