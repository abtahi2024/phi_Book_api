from rest_framework import serializers
from books.models import Category,Book,Review,BookImages
from decimal import Decimal
from django.conf import settings
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','description','book_count']
    
    book_count=serializers.IntegerField(read_only=True,help_text='Return the number books in this category')

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookImages
        fields=['id','image']


class BookSerializers(serializers.ModelSerializer):
    images=BookImageSerializer(many=True,read_only=True)
    class Meta:
        model=Book
        fields=['id','name','description','price','stock','category','price_with_tex','images']

    price_with_tex=serializers.SerializerMethodField(method_name='calculate_tex')
    def calculate_tex(self,product):
        return round(product.price*Decimal(1.1),2)
    
    def validate_price(self, price):
        if price<0:
            raise serializers.ValidationError('price could not be negative')
        return price



class SimplerUserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(method_name='get_current_user_name')
    class Meta:
        model=get_user_model()
        fields=['id','name']
    
    def get_current_user_name(self,obj):
        return obj.get_full_name()

class ReviewSerilizers(serializers.ModelSerializer):
    user=serializers.SerializerMethodField(method_name='get_user')
    class Meta:
        model=Review
        fields=['id','user','book','ratings','comment']
        read_only_fields=['user','book']
    
    def get_user(self,obj):
        return SimplerUserSerializer(obj.user).data

    def create(self, validated_data):
        book_id=self.context['book_id']
        return Review.objects.create(book_id=book_id,**validated_data)
    
