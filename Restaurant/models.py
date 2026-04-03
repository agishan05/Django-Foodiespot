from django.db import models

class Food(models.Model):

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    image = models.CharField(max_length=200)  

    def __str__(self):
        return self.name


class Order(models.Model):

    food = models.ForeignKey(Food,on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name