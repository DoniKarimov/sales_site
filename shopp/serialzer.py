from rest_framework import serializers
from .models import Category, Product, Product_img
from .models import CustomUser

class CustomUserSer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  
        fields = ['username', 'password','photo', 'is_active']
        extra_kwargs = {'password' : {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class Change_password(serializers.Serializer):
    old_password = serializers.CharField(max_length = 25)
    new_password = serializers.CharField(max_length = 25)
    coniform_password = serializers.CharField(max_length = 25)


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category     
        fields = ['id', 'name', 'rasm','parent']
    

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'sharx', 'price', 'category', 'user'] 
        extra_kwargs = {'user':{'read_only': True}}
    
    def create(self, validated_data):
        user = self.context['request'].user
        new_product = Product.objects.create(user=user, **validated_data)
        return new_product
    

class Product_imgSer(serializers.ModelSerializer):
    class meta:
        model = Product_img
        fields = ['rasm', 'product']

# class SavatSer(serializers.ModelSerializer):
#     class Meta:
#         model = Savat
#         fields = ['soni']        

