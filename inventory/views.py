from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self,request, *args, **kwargs):
        item_id = kwargs['pk']
        item = cache.get(f'item_{item_id}')

        if not item:
            response = super().retrieve(request,*args,**kwargs)
            cache.set(f'item_{item_id}',response.data, timeout = 3600)
            return response 
        
        return Response(item)



