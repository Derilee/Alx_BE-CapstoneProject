from django.urls import path
from .views import InventoryItemListView, InventoryItemCreateView, InventoryItemRetrieveUpdateDestroyView, InventoryChangeHistoryView, InventoryCurrentLevelsView

#an endpoint that links a url to a view
urlpatterns = [
    path('inventory/', InventoryItemListView.as_view(), name='inventory_list'),
    path('inventory/create/', InventoryItemCreateView.as_view(), name='inventory_create'),
    path('inventory/<int:pk>/', InventoryItemRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),
    path('inventory/history/', InventoryChangeHistoryView.as_view(), name='inventory_history'),
    path('inventory/current-levels/', InventoryCurrentLevelsView.as_view(), name='inventory_levels'),
]