from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineAminInLine(admin.TabularInline):
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAminInLine, )

admin.site.register(Order, OrderAdmin)