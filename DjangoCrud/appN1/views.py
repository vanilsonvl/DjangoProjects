from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Product
from.forms import BrandForm, ProductForm


def register_brand(request, template_name='brand/brand_form.html'):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_marcas')
    return render(request, template_name, {'form': form})


def brand_list(request, template_name='brand/brand_list.html'):
    query = request.GET.get('buscar')
    if query:
        brands = Brand.objects.filter(name__iexact=query)
    else:
        brands = Brand.objects.all()
    return render(request, template_name, {'brands': brands})


def edit_brand(request, pk, template_name='brand/brand_form.html'):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('lista_marcas')
    else:
        form = BrandForm(instance=brand)
    return render(request, template_name, {'form': form})


def remove_brand(request, pk, template_name='brand/brand_delete.html'):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('lista_marcas')
    return render(request, template_name, {'brand': brand})


def list_product_brand(request, pk, template_name='brand/product_brand_list.html'):
    products = Product.objects.filter(brand=pk)
    return render(request, template_name, {'products': products})


def register_product(request, template_name='product/product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, template_name, {'form': form})


def product_list(request, template_name='product/product_list.html'):
    query = request.GET.get('buscar')
    if query:
        products = Product.objects.filter(description__iexact=query)
    else:
        products = Product.objects.all()
    return render(request, template_name, {'products': products})


def edit_product(request, pk, template_name='product/product_form.html'):
    car = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProductForm(instance=car)
    return render(request, template_name, {'form': form})


def remove_product(request, pk, template_name='product/product_delete.html'):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('lista_produtos')
    return render(request, template_name, {'product': product})

