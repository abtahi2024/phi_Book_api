from rest_framework import serializers
from order.models import Cart ,CartItem, Order,OrderItem
from books.models import Book
from order.services import OrderService

class EmptySerializer(serializers.Serializer):
    pass

class SimpleBookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','name','price']


class AddCartItemSerializer(serializers.ModelSerializer):
    book_id=serializers.IntegerField()
    class Meta:
        model=CartItem
        fields=['id','book_id','quantity']
    
    def save(self, **kwargs):
        cart_id=self.context['cart_id']
        book_id=self.context['book_id']
        quantity=self.context['quantity']

        try:
            cart_item=CartItem.objects.get(cart_id=cart_id,book_id=book_id,quantity=quantity)
            cart_item.quantity+=quantity
            self.instance=cart_item.save()
        except CartItem.DoesNotExist:
            self.instance=CartItem.objects.create(cart_id=cart_id,**self.validated_data)
        return self.instance
    def validate_book_id(self, value):
        if not Book.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f'Book with id{value} does not Exists')
        return value
    

class UpdataCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['quantity']

class CartItemSerializer(serializers.ModelSerializer):
    book=SimpleBookSerializers()
    total_price=serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model=CartItem
        fields=['id','book','quantity','book','total_price']
    
    def get_total_price(self,cart_item:CartItem):
        return cart_item.quantity*cart_item.book.price
    

class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)
    total_price=serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model=Cart
        fields=['id','user','items','total_price']
        read_only_fields=['user']

    def get_total_price(self,cart:Cart):
        return sum([item.book.price*item.quantity for item in cart.items.all()])


class CreateOrderSerializer(serializers.Serializer):
    cart_id=serializers.UUIDField()
    def validate_cart_id(self,cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('no cart found with this id')
        if not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError('cart is empty')
        return cart_id
    
    def create(self, validated_data):
        user_id=self.context['user_id']
        cart_id=validated_data['cart_id']
        try:
            order=OrderService.cerate_order(user_id=user_id,cart_id=cart_id)
            return order
        except ValueError as e:
            raise serializers.ValidationError(str(e))
    
    def to_representation(self, instance):
        return OrderSerializer(instance).data

class OrderItemSerializer(serializers.ModelSerializer):
    book=SimpleBookSerializers()
    class Meta:
        model=OrderItem
        fields=['id','book','price','quantity','total_price']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['status']
    


class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=['id','user','status','total_price','created_at','items']