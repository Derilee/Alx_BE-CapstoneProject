from .models import InventoryItem, InventoryChangeHistory
from rest_framework import serializers
from users.serializers import UserSerializer


#Serializes the Inventory item model
class InventoryItemSerializer(serializers.ModelSerializer):
    #uses UserSerializer to display the details of who own owns the Inventory Item
    owner = UserSerializer(read_only=True) #read-only means the owner field cannot be modified through the API.
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity', 'price', 'category', 'date_added', 'last_updated', 'owner']

    #a method to validate price can't be a negative value
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price can't be a negative value") 
        return value


#Serializes the Inventory Change History model
class InventoryChangeHistorySerializer(serializers.ModelSerializer):
    changed_by = UserSerializer(read_only=True) #uses UserSerializer to display the details of the user who made the change
    class Meta:
        model = InventoryChangeHistory
        fields = ['item', 'old_quantity', 'new_quantity', 'change_date', 'changed_by']


#Serializes certain fields in the inventory item
class InventoryCurrentLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity']
