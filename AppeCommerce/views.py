from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Product, Category, Customer, Cart, models
from .forms import ProductForm, CategoryForm, CustomerForm, SearchForm

def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})

def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form': form})

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm()
    return render(request, 'customer.html', {'form': form})

def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.filter(name__icontains=query)
        return render(request, 'search_results.html', {'results': results})

def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if product not in cart.products.all():
        cart.products.add(product)
        cart.total += product.price
        cart.save()
    return render(request, 'cart.html', {'cart': cart})

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart.products.clear()
    cart.total = 0
    cart.save()
    return render(request, 'checkout.html')

def remove_from_cart(request, id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(user=request.user)
    if product in cart.products.all():
        cart.products.remove(product)
        cart.total -= product.price
        cart.save()
    return render(request, 'cart.html', {'cart': cart})

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')