import requests
from django.contrib.auth.models import Group, User


from accounts.models import ChiefProfile, Profile
from api.v1.accounts.serializer import LoginSerializer, RegisterSerializer, UserDetailsSerializer
from general.encryption import decrypt, encrypt
from general.functions import generate_serializer_errors

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        username = request.data['username']
        password = request.data['password']
        fullname = request.data['fullname']
        phone = request.data['phone']
        if Profile.objects.filter(username=username, phone=phone).exists():
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : "Profile is already exists"
                }
            }
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            encpass = encrypt(password)
            if phone.isdigit():
                profile = Profile.objects.create(
                    user = user,
                    name = fullname,
                    username = username,
                    password = encpass,
                    phone = phone
                )
            else:
                profile = Profile.objects.create(
                    user = user,
                    name = fullname,
                    password = encpass,
                    email = phone,
                )
            protocol = "http://"
            web_host = request.get_host()
            request_url = protocol + web_host + "/api/v1/accounts/token/"
            response = requests.post(
                        request_url,
                        data = {
                            "username" : username,
                            "password" : password,
                        }
                    )

            response = response.json()
            response_data = {
                "StatusCode" : 6000,
                "data" : {
                    "title" : "success",
                    "acess_token" : response,
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def profile_login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        phone = request.data['phone']
        password = request.data['password']
        if phone.isdigit():
            if Profile.objects.filter(phone=phone).exists():
                profile = Profile.objects.get(phone=phone)
                decrpass = decrypt(profile.password)
                if password == decrpass:
                    protocol = "http://"
                    web_host = request.get_host()
                    request_url = protocol + web_host + "/api/v1/accounts/token/"
                    response = requests.post(
                        request_url,
                        data={
                            "username": profile.username,
                            "password": password,
                        }
                    )
                    response = response.json()
                    response_data = {
                        "StatusCode" : 6000,
                        "data" : {
                            "title" : "Success",
                            "acess_token" : response,
                        }
                    }
                else:
                    response_data = {
                        "StatusCode" : 6001,
                        "data" : {
                            "title" : "Failed",
                            "message" : "Incorrecte Password"
                        }
                    }
            else:
                response_data = {
                    "StatusCode" : 6001,
                    "data" : {
                        "title" : "Failed",
                        "message" : "Profile not found"
                    }
                }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : "Enter a valid phone number",
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data" : {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            },
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    serialized_data = UserDetailsSerializer(context={"request" : request})
    response_data = {
        "StatusCode" : 6000,
        "data" : serialized_data
    }

    return Response(response_data, status=status.HTTP_200_OK) 
    



    
            



    


