from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.parsers import JSONParser

from .models import CartItem

from .serializers import CartSerializer
from rest_framework.response import Response

from .models import Orders
from .serializers import OrderSerializer

class CartAddView(generics.GenericAPIView):

    def post(self,request):
        data = {}
        if request.method == 'POST':
            add_cart = JSONParser().parse(request)

            serializer = CartSerializer(data=add_cart)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data['responseCode'] = status.HTTP_200_OK
                data["typeCode"] = status.HTTP_201_CREATED
                data['CartDetails'] = "Item added to cart successfully"
                return Response(data=data)
            else:
                data['responseCode'] = status.HTTP_400_BAD_REQUEST
                data["typeCode"] = status.HTTP_400_BAD_REQUEST
                data['ItemDetails'] = "Invalid data"
                return Response(data=data)
        data["responseCode"] = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(data=data)


class GetAllOrdersView(generics.RetrieveAPIView ):
    serializer_class =  CartSerializer

    def get(self,request):
        data = {}
        item_data = CartItem.objects.all()
        print(item_data)
        if item_data:

            serializer = CartSerializer(data=item_data,many=True)
            serializer.is_valid()
            data["responseCode"] = status.HTTP_200_OK
            data["typeCode"] = status.HTTP_200_OK
            data['message'] = "Success"
            data['userData'] = serializer.data
            return Response(data=data)
        else:
            data["responseCode"] = status.HTTP_400_BAD_REQUEST
            data["typeCode"] = status.HTTP_400_BAD_REQUEST
            data['message'] = "id not existing"
            return Response(data=data)


class GetOrderDetailsView(generics.RetrieveAPIView ):
    serializer_class = OrderSerializer

    def get(self,request):
        data = {}
        user_id = request.GET.get('userId')
        order_data = Orders.objects.filter(userId=user_id)
        if order_data:

            serializer = OrderSerializer(data=order_data,many=True)
            serializer.is_valid()
            data["responseCode"] = status.HTTP_200_OK
            data["typeCode"] = status.HTTP_200_OK
            data['message'] = "Success"
            data['userData'] = serializer.data
            return Response(data=data)
        else:
            data["responseCode"] = status.HTTP_400_BAD_REQUEST
            data["typeCode"] = status.HTTP_400_BAD_REQUEST
            data['message'] = "id not existing"
            return Response(data=data)


class AddOrderView(generics.GenericAPIView):

    def post(self,request):
        data = {}
        if request.method == 'POST':
            create_order = JSONParser().parse(request)
            serializer = OrderSerializer(data=create_order)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                cart_data = CartItem.objects.filter(itemId=create_order['itemId'])
                if cart_data:
                    cart_data.delete()
                data['responseCode'] = status.HTTP_200_OK
                data["typeCode"] = status.HTTP_201_CREATED
                data['OrderDetails'] = "Order created successfully"
                return Response(data=data)
            else:
                data['responseCode'] = status.HTTP_400_BAD_REQUEST
                data["typeCode"] = status.HTTP_400_BAD_REQUEST
                data['ItemDetails'] = "Invalid data"
                return Response(data=data)
        data["responseCode"] = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(data=data)