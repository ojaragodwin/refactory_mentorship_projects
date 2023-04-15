from django.db import models

# Create your models here.
#models means description on the database where we store things
#models are python classes
class Category(models.Model):
    name = models.CharField(max_length= 50, null = True, blank= True)
#this method gives human readable name for the object of the class which is our category
    def __str__(self): 
        return self.name
    #after defining the model you have to go back to the terminal python manage.py makemigrations then
    #python manage.py migrate.

class Product(models.Model):
    #here we are connecting products model to category model
    #a foreign key is a column in one table being referenced in another table
    Category_name = models.ForeignKey(Category,on_delete= models.CASCADE,null=True, blank=True)

    item_name = models.CharField(max_length= 50, null = True, blank= True)
    total_quantity = models.IntegerField(default= 0, null = True, blank= True)
    issued_quantity = models.IntegerField(default= 0, null = True, blank= True)
    received_quantity =  models.IntegerField(default= 0, null = True, blank= True)
    unit_price =  models.IntegerField(default= 0, null = True, blank= True)
    manufacturer = models.CharField(max_length= 50, null = True, blank= True)
    brand = models.CharField(max_length= 50, null = True, blank= True)

#this method gives human readable name for the object of the class which is our category
    def __str__(self): 
        return self.item_name
    
class Sale(models.Model):
    # the item name, the price, purchasers name, date of purchase, quantity purchased,
    item = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0,null=False,blank=True)
    amount_received =models.IntegerField(default=0, null = False, blank= True)
    issued_to=models.CharField(max_length= 50, null = True, blank= True)
    unit_price =  models.IntegerField(default= 0, null = True, blank= True)
    #date = models.DateTimeField(auto_now_add= True)
    #method below calculates sales total
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    #the method below calculates change
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    #def get_vat():
        pass
    def __str__(self):
        return self.item.item_name
    