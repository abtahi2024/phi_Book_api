from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from order.models import Cart,Order,CartItem,OrderItem
from order.serializers import CartSerializer,CartItemSerializer,AddCartItemSerializer,UpdataCartItemSerializer,OrderSerializer,CreateOrderSerializer,UpdateOrderSerializer,EmptySerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from order.services import OrderService
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# Create your vews here.

class CartViewSet(CreateModelMixin,GenericViewSet,RetrieveModelMixin,DestroyModelMixin):
    serializer_class=CartSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        if getattr(self,'swagger_fake_view', False):
            return Cart.objects.none()
        return Cart.objects.prefetch_related('items__book').filter(user=self.request.user)
    
    @swagger_auto_schema(operation_summary='user Post and Add the Cart')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Every one can see the cart')
    def list(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='user can Delete')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='show the cart')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class CartItemViewSet(ModelViewSet):
    http_method_names=['get','post','patch','delete']
    
    def get_serializer_class(self):
        if self.request.method== 'POST':
            return AddCartItemSerializer
        elif self.request.method=='PATCH':
            return UpdataCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        if getattr(self,'swagger_fake_view',False):
            return context
        return {'cart_id': self.kwargs.get('cart_pk')}

    def get_queryset(self):
        return CartItem.objects.select_related('book').filter(cart_id=self.kwargs.get('cart_pk'))
    
    @swagger_auto_schema(operation_summary='Views the Cart id')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='user add cart id and show items')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class OrderViewset(ModelViewSet):
    http_method_names=['get','post','patch','head','options']

    @swagger_auto_schema(operation_summary='user can cancel the Cart')
    @action(detail=True,methods=['post'])
    def cancel(self,request,pk=None):
        order=self.get_object()
        OrderService.cancel_order(order=order,user=request.user)
        return Response({'status':'Order canceled'})
    
    @swagger_auto_schema(operation_summary='Admin can Update')
    @action(detail=True,methods=['patch'])
    def update_status(self,request,pk=None):
        order=self.get_object()
        serializer=UpdateOrderSerializer(order,data=request.data,pertial=True)
        serializer.is_valid(raise_exception=True)
        return Response({'status':f'order status updated to {request.data['status']}'})
    
    def get_permissions(self):
        if self.action in ['update_status','destroy']:
            return[IsAdminUser()]
        return [IsAuthenticated()]
        

    def get_serializer_class(self, *args, **kwargs):
        if self.action=='cancel':
            return EmptySerializer
        
        if self.action=='create':
            return CreateOrderSerializer
        elif self.action=='update_status':
            return UpdateOrderSerializer
        return OrderSerializer
    
    def get_serializer_context(self):
        if getattr(self, 'swagger_fake_view', False):
            return super().get_serializer_context()
        return {'user_id':self.request.user.id,'user':self.request.user}
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__book').all()
        return Order.objects.prefetch_related('items__book').filter(user=self.request.user)
    
    @swagger_auto_schema(operation_summary='Every one can see the order')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary='Cart order id POST')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    