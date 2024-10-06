from typing import Any, Iterable
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

#get the user model and assigns it to User
User = get_user_model()

#Inventory item model with its field
class InventoryItem(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) #auto_now_add means the date field can not be modified
    last_updated = models.DateTimeField(auto_now=True) #auto_now means the date can be modified on each update
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory_items') #this field establishes a many to one relationship between the InventoryItem and the User.

    #a string representation method that makes the name field readable and displays it when printing the model
    def __str__(self):
        return self.name


#To track changes in the quantity field, before saving an InventoryItem, store the quantity as old_quantity to track changes
@receiver(pre_save, sender=InventoryItem)
def old_quantity_change(sender, instance, **kwargs):
    if instance.pk: #check if the instance exist in the DB
        old_instance = InventoryItem.objects.get(pk=instance.pk) #if the instance exist, get the instance
        instance.old_quantity = old_instance.quantity #store the gotten quantity as old quantity


#Inventory change history model with its field
class InventoryChangeHistory(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='items_log')
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_change')
    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()
    change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
    
#anytime there is a change in the quantity of an inventory item, store the change from old_quantity to new_quantity
@receiver(post_save, sender=InventoryItem)
def inventory_change_history(sender, instance, created, **kwargs):
    if not created and instance.old_quantity != instance.quantity: #check if there is a change in the quantity of an item
        InventoryChangeHistory.objects.create(
            item=instance,
            changed_by=instance.owner, #track the owner who made the change in the inventory item
            old_quantity=instance.old_quantity, #save the previous quantity
            new_quantity=instance.quantity #save the new quantity
        )

