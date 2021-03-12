from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    item = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product_detail.html', {'item': item})


def category_list(request,category_slug):
    category_item = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category_item)

    return render(request,'store/category_slug.html',{'products':products, 'category':category_item})

