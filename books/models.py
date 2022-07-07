from django.db import models

# Create your models here.
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Book(AbstractBaseModel):
    title = models.CharField(max_length=255)
    year_published = models.CharField(max_length=4)
    publisher = models.CharField(max_length=200)
    category = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title


class Customer(AbstractBaseModel):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Burgain(AbstractBaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    your_price = models.FloatField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.name} burgained {self.book.title} to {str(self.your_price)}"