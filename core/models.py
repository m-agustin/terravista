from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class Item(models.Model):  # Items that we're selling
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class OrdersItem(models.Model):  # link between the item and the order
    item = models.ForeignKey(Item, on_delete=CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):  # shopping cart
    # Will load the shopping cart when user logs-in
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrdersItem)
    # Show the date item was created
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    orderered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
