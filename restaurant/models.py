from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateField()

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'