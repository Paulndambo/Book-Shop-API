from django.contrib import admin
from .models import Book, Burgain, Customer
# Register your models here.
admin.site.register(Book)
admin.site.register(Burgain)
admin.site.register(Customer)