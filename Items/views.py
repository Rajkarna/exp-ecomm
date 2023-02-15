from django.db.models import Avg
from django.shortcuts import render

# Create your views here.
from Cart.models import Orders
from Items.serializers import ItemSerializer, RatingSerializer, ItemRateSerializer
from rest_framework import generics, status

from Items.models import ItemsTable, RatingTable
from rest_framework.parsers import JSONParser
from rest_framework.response import Response



class GetAllItemsView(generics.RetrieveAPIView ):
    serializer_class =  ItemSerializer

    def get(self,request):
        data = {}
        item_data = ItemsTable.objects.all()
        if item_data:

            serializer = ItemSerializer(data=item_data,many=True)
            serializer.is_valid()
            data["responseCode"] = status.HTTP_200_OK
            data["typeCode"] = status.HTTP_200_OK
            data['message'] = "Success"
            data['ItemData'] = serializer.data
            return Response(data=data)
        else:
            data["responseCode"] = status.HTTP_400_BAD_REQUEST
            data["typeCode"] = status.HTTP_400_BAD_REQUEST
            data['message'] = "id not existing"
            return Response(data=data)


class GetItemDetailsView(generics.RetrieveAPIView ):
    serializer_class = ItemSerializer

    def get(self,request):
        data = {}
        item_id = request.GET.get('ItemId')
        item_data = ItemsTable.objects.filter(itemId=item_id)
        if item_data:

            serializer = ItemSerializer(data=item_data,many=True)
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


class ItemAddView(generics.GenericAPIView):

    def post(self,request):
        data = {}
        if request.method == 'POST':
            create_item = JSONParser().parse(request)

            serializer = ItemSerializer(data=create_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data['responseCode'] = status.HTTP_200_OK
                data["typeCode"] = status.HTTP_201_CREATED
                data['ItemDetails'] = "Item created successfully"
                return Response(data=data)
            else:
                data['responseCode'] = status.HTTP_400_BAD_REQUEST
                data["typeCode"] = status.HTTP_400_BAD_REQUEST
                data['ItemDetails'] = "Invalid data"
                return Response(data=data)
        data["responseCode"] = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(data=data)


class AddRatingView(generics.GenericAPIView):

    def post(self,request):
        data = {}
        if request.method == 'POST':
            create_item = JSONParser().parse(request)

            serializer = RatingSerializer(data=create_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data['responseCode'] = status.HTTP_200_OK
                data["typeCode"] = status.HTTP_201_CREATED
                data['ItemDetails'] = "Rating updated successfully"
                return Response(data=data)
            else:
                data['responseCode'] = status.HTTP_400_BAD_REQUEST
                data["typeCode"] = status.HTTP_400_BAD_REQUEST
                data['ItemDetails'] = "Invalid data"
                return Response(data=data)
        data["responseCode"] = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(data=data)


class GetAvgRatingView(generics.RetrieveAPIView ):
    serializer_class = ItemSerializer

    def get(self,request):
        data = {}
        item_id = request.GET.get('ItemId')
        item_data = RatingTable.objects.filter(itemId=item_id).annotate(avgRating=Avg('rating'))
        print(item_data)
        if item_data:

            serializer = ItemRateSerializer(data=item_data,many=True)
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


class GetItemReviewsView(generics.RetrieveAPIView ):
    serializer_class = ItemSerializer

    def get(self,request):
        data = {}
        item_id = request.GET.get('itemId')
        print(type(item_id))
        item_data = RatingTable.objects.filter(itemId=item_id)
        print(type(item_data))
        if item_data:

            serializer = RatingSerializer(data=item_data,many=True)
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


class UserCountAPI(generics.GenericAPIView):


    def get(self, request):
        data = {}
        count_data = {}
        if request.method == 'GET':
            item_id = request.GET.get('itemId')
            item_check = ItemsTable.objects.get(itemId=item_id)

            item_check.userCount = item_check.userCount + 1
            item_check.save(update_fields=("userCount",))
            data["responseCode"] = status.HTTP_200_OK
            data["typeCode"] = status.HTTP_200_OK
            data["message"] = 'Success'
            return Response(data=data)

        else:
            data["responseCode"] = status.HTTP_405_METHOD_NOT_ALLOWED
            data["typeCode"] = status.HTTP_405_METHOD_NOT_ALLOWED
            data['errorMessage'] = "Method is not allowed here"
            return Response(data=data)