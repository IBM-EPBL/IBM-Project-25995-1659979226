from dataclasses import field
from statistics import mode
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import User, OTP
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','phone_number')

        extra_kwargs = {
            'username' : {
                'required' : True,
                'validators' : [
                    UniqueValidator(
                        User.objects.all(),
                        "A user with that username already exists!"
                    )
                ]
            },
            'password' : {'write_only' : True},
            'email' : {
                'required' : True,
                'allow_blank' : False,
                'validators' : [
                    UniqueValidator(
                        User.objects.all(),
                        "A user with that email already exists!"
                    )
                ]
            },
            'phone_number' : {
                'required' : True,
                'validators' : [
                    UniqueValidator(
                        User.objects.all(),
                        "A user with that phone number already exists!"
                    )
                ]
            },
        }
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return User.objects.create(**validated_data)

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('phone_number',)
        extra_kwargs = {
            'phone_number' : {
                    'required' : True,
                    'validators' : [
                        UniqueValidator(
                            OTP.objects.all(),
                            "Try again after a minute!"
                        )
                    ]
                }
        }
        
    def create(self, validated_data):
        username = User.objects.filter(phone_number=validated_data['phone_number']).values()
        print(username)
        if not username:
            msg = ('Phone number doesn\'t exist!')
            raise serializers.ValidationError(msg, code='authorization')
        if username[0].get('otp'):
            msg = ('Account already verified!')
            raise serializers.ValidationError(msg, code='authorization')
        else:
            validated_data['_otp'] = OTP.generate_otp()
            validated_data['expiration_date'] = OTP.generate_expdate()
            validated_data['expiration_time'] = OTP.generate_exptime()

        return OTP.objects.create(**validated_data)

class OTPVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.IntegerField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        otp = attrs.get('otp')
        org = OTP.objects.filter(phone_number=phone_number, _otp=otp)
        if not org:
            msg = ('Invalid OTP!')
            raise serializers.ValidationError(msg, code='authorization')
        else:
            user = User.objects.get(phone_number=phone_number)
            user.otp = True
            user.save()
        return attrs

class PasswordUpdateSerializer(serializers.Serializer):
    password = serializers.CharField()

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password',instance.password))
        instance.save()
        return instance

class PhoneNumberUpdateSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number',instance.phone_number)
        instance.save()
        return instance