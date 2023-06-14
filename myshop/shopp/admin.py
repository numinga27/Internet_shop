from django.contrib import admin
from .models import User, Product, Cart, CartProduct, Favorite, Purchase, PurchaseProduct

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Favorite)
admin.site.register(Purchase)
admin.site.register(PurchaseProduct)