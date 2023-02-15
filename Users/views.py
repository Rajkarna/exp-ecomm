import bcrypt
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status

from Users.serializers import RegisterSerializer,LoginSerializer
from rest_framework.parsers import JSONParser

from Users.models import User
from rest_framework.response import Response



class GenerateKey:
    @staticmethod
    def hash_value(password):
        return bcrypt.hashpw(password, bcrypt.gensalt(4))

class RegisterView(generics.GenericAPIView, ):
    serializer_class = RegisterSerializer

    def post(self, request):
        result_object = {}
        data = {}
        keygen = GenerateKey()
        user_data_request = JSONParser().parse(request)
        passwords = user_data_request['password']
        hash_password = keygen.hash_value(user_data_request['password'].encode('utf-8')).decode('utf-8')
        user_data_request.update({'password': hash_password})
        serializer = self.serializer_class(data=user_data_request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])
        tokens = user.tokens()
        result_object['id'] = user.id
        result_object['userName'] = user.userFirstName
        result_object['lastName'] = user.lastName
        result_object['address'] = user.address
        result_object['dob'] = user.dob
        result_object['phoneNumber'] = user.phoneNumber
        result_object['created_at'] = user.created_at
        result_object['updated_at'] = user.updated_at
        data["responseCode"] = status.HTTP_200_OK
        data["typeCode"] = status.HTTP_201_CREATED
        data['message'] = "Your account created successfully"
        data['userData'] = result_object
        data['tokens'] = tokens

        return Response(data=data)


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = {}
        result_object = {}
        try:
            user = User.objects.get(email__exact=request.data['email'])
        except ObjectDoesNotExist:
            data["responseCode"] = status.HTTP_400_BAD_REQUEST
            data["typeCode"] = status.HTTP_404_NOT_FOUND
            data["details"] = 'User does not exist '
            return Response(data=data)
        print(bcrypt.checkpw(request.data['password'].encode('utf-8'), user.password.encode('utf-8')))
        if user is not None and bcrypt.checkpw(request.data['password'].encode('utf-8'), user.password.encode('utf-8')):
            tokens = user.tokens()
            result_object['id'] = user.id
            result_object['userFirstName'] = user.userFirstName
            result_object['lastName'] = user.lastName
            result_object['address'] = user.address
            result_object['dob'] = user.dob
            result_object['phoneNumber'] = user.phoneNumber
            result_object['created_at'] = user.created_at
            result_object['updated_at'] = user.updated_at
            data["responseCode"] = status.HTTP_200_OK
            data["typeCode"] = status.HTTP_200_OK
            data['message'] = "Login successfully"
            data['userData'] = result_object
            data['tokens'] = tokens
            return Response(data=data)
        else:
            data["responseCode"] = status.HTTP_400_BAD_REQUEST
            data["typeCode"] = status.HTTP_404_NOT_FOUND
            data["details"] = 'Invalid credentials, try again'
            return Response(data=data)


class LogoutView(generics.GenericAPIView):
    def post(request):
        data = {}
        if request.method == 'POST':
            user_id = request.GET.get('userId')
            data["responseCode"] = status.HTTP_200_OK
            data["message"] = "Logout successfully"
            return Response(data=data)
        data["responseCode"] = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(data=data)