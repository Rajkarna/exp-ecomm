from rest_framework import serializers
from Cart.models import CartItem,Orders



class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'