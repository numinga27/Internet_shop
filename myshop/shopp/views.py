from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page

from .models import Cart, Product,CartProduct,Favorite,Purchase, PurchaseProduct


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    return redirect('cart')



def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(user=request.user)
    cart_product = CartProduct.objects.get(cart=cart, product=product)
    if cart_product.quantity > 1:
        cart_product.quantity -= 1
        cart_product.save()
    else:
        cart_product.delete()
    return redirect('cart')



def add_to_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user)
    favorite.products.add(product)
    return redirect('favorite')



def remove_from_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite = Favorite.objects.get(user=request.user)
    favorite.products.remove(product)
    return redirect('favorite')

def add_purchase(request):
    cart = Cart.objects.get(user=request.user)
    purchase = Purchase.objects.create(user=request.user, total_price=cart.total_price())
    for cart_product in cart.cartproduct_set.all():
        PurchaseProduct.objects.create(purchase=purchase, product=cart_product.product, quantity=cart_product.quantity, price=cart_product.product.price)
        cart_product.delete()
    return redirect('purchase_history')