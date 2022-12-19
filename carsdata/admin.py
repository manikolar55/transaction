from django.contrib import admin

from .models import Block, CarsBlock, WishListBlock, WishListCarsBlock

# Register your models here.

admin.site.register(Block)
admin.site.register(CarsBlock)
admin.site.register(WishListBlock)
admin.site.register(WishListCarsBlock)
