from django_filters import rest_framework as filters
from .models import InventoryItem


#A filter class that handles filtering operation for inventory item
class InventoryItemFilter(filters.FilterSet):
    #Custom filter field that calls the filter_low_stock method to filter items based on low stock status being true or false
    low_stock = filters.BooleanFilter(method='filter_low_stock')
    #a custom filter field to filter category field 
    category = filters.CharFilter(field_name='category', lookup_expr='iexact') #iexact performs case-insensitive filtering

    class Meta:
        model = InventoryItem
        fields = {
            'price': ['lte', 'gte'], #filter price less than or greater than an amount
        }

    # a method to filter out low stock inventory items with quantity less than a threshold
    def filter_low_stock(self, queryset, name, value):
        threshold = 10 #threshold amount set to 10
        if value:
            return queryset.filter(quantity__lt=threshold) #return a filtered queryset of quantity less than the threshold
        return queryset