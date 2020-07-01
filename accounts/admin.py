from django.contrib import admin
from .models import Customer, Product, Order, Tag, Subcat, Cat

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Subcat)
admin.site.register(Cat)

