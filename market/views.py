from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from market.models import Category, Product, Basket
from users.models import User


# Create your views here.

def index(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    items_per_page = 3
    paginator = Paginator(products, items_per_page)
    paginator_page = paginator.page(page_number)

    content = {
        'title': 'Mark_Index',
        'products': paginator_page,
        'categories': Category.objects.all(),
    }
    return render(request, 'market/index.html', context=content)


def goods(request):
    pass


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

