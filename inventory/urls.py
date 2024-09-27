from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
]



# urlpatterns = [
#     path = ('items/',ItemViewSet.as_view({'get' : 'list', 'post' : 'create'}), name = 'item-list'),
#     path = ('items/<int:pk>/',ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='item-detail')
# ]
