from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

from .serializer import RegisterSerializer, OTPSerializer, OTPVerifySerializer, PasswordUpdateSerializer, PhoneNumberUpdateSerializer
from .models import OTP, User
from datetime import datetime
# from . import dbQuery as db



@api_view(['POST'])
def login_user(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _,token = AuthToken.objects.create(user)

    return Response({
        'user-info' : {
            'id' : user.id,
            'name' : user.username,
            'email' : user.email
        },
        'token' : token
    })

@api_view(['GET'])
def get_user_detail(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user-info' : {
                'id' : user.id,
                'username' : user.username,
                'email' : user.email,
                'phone_number' : user.phone_number
            },
        }) 
    
    return Response({'error' : 'User not authenticated!'}, status=400)

@api_view(['PUT'])
def update_password(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        serializer = PasswordUpdateSerializer(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'user-info' : {
                'username' : user.username,
            },
            'message' : "Password updated successfully!"
        })
    return Response({'error' : 'User not authenticated!'}, status=400)

@api_view(['PUT'])
def update_phonenumber(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        serializer = PhoneNumberUpdateSerializer(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'user-info' : {
                'username' : user.username,
            },
            'message' : "Phone Number updated successfully!"
        })
    return Response({'error' : 'User not authenticated!'}, status=400)

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _,token = AuthToken.objects.create(user)
    # query = "INSERT INTO USERS(user_id,username,first_name,last_name,email,phone_number,password) values(%s,%s,%s,%s,%s,%s,%s)"%(user.id,user.username,user.first_name,user.last_name,user.email,user.phone_number,user.password)
    # status = db.insertQuery(query)

    return Response({
        'user-info' : {
            'id' : user.id,
            'username' : user.username,
            'email' : user.email,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'phone_number' : user.phone_number
        },
        'token' : token
        })
        
@api_view(['POST'])
def get_otp(request):
    OTP.objects.filter(expiration_time__lt=datetime.now().time()).delete()
    serializer = OTPSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    otp = serializer.save()
    return Response({
        #'username' : otp.username,
        'otp' : otp._otp
    })

@api_view(['POST'])
def verify_otp(request):
    OTP.objects.filter(expiration_time__lt=datetime.now().time(), expiration_date__exact=datetime.now().date()).delete()
    serializer = OTPVerifySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({
        'message' : 'Account verified!'
    })