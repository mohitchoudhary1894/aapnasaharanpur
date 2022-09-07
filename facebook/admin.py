from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(registration)
admin.site.register(Category)
admin.site.register(product)
admin.site.register(order)

