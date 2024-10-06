from django.shortcuts import render
from .models import InventoryItem, InventoryChangeHistory
from .serializers import InventoryItemSerializer, InventoryChangeHistorySerializer, InventoryCurrentLevelsSerializer
from .filters import InventoryItemFilter 
from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


#pagination class
class InventoryItemPagination(PageNumberPagination):
    page_size = 10


#checks if the user is the owner of the inventory
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


#ApiView to create inventory item
class InventoryItemCreateView(generics.CreateAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    #checks if the user is authenticated before creating an inventory item
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("only Authenticated users can create inventory item")
        return serializer.save(owner=self.request.user) #saves the user in the owner field
    

#ApiView to list inventory item, perform filtering, ordering and pagination
class InventoryItemListView(generics.ListAPIView):
    queryset = InventoryItem.objects.all().order_by('name') #retrieves inventory item model and sets a default order for the model to ensure pagination works well
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = InventoryItemFilter 
    ordering_fields = ['name', 'quantity', 'price', 'date_added']
    pagination_class = InventoryItemPagination


#ApiView to retrieve, Update and Delete inventory item
class InventoryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsOwner] #permits only authenticated user and owner of the inventory to update/delete items


#ApiView to show Inventory change history
class InventoryChangeHistoryView(generics.ListAPIView):
    queryset = InventoryChangeHistory.objects.all()
    serializer_class = InventoryChangeHistorySerializer
    permission_classes = [IsAuthenticated]


#ApiView to show inventory current levels
class InventoryCurrentLevelsView(generics.ListAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryCurrentLevelsSerializer
    permission_classes = [IsAuthenticated]