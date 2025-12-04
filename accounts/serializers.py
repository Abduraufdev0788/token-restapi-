from rest_framework import serializers
from  django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RegisterSerializers(serializers.ModelSerializer):

    confirm = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm', 'email', 'first_name', 'last_name']

    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError("parollar mos emas!")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm')
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
    

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(max_length = 128)
        
    
        