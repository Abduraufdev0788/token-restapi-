from rest_framework import serializers
from  django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "role", "groups", "user_permissions"]

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


class ProfileUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "role", "groups", "user_permissions"]
        extra_kwargs = {
            "username": {
                "required": False
            }
        }


class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)
    confirm = serializers.CharField(max_length=128)
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm']:
            raise serializers.ValidationError('password and confirm are nor the same value.')
        
        return super().validate(attrs)
    

class AdminDashboardserializer(serializers.Serializer):
    total_users = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"
       

    def get_total_users(self,obj):
        return User.objects.count()
    
    def get_users(self, obj):
        return User.objects.all().values(
            'id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', "password", "role", "groups", "user_permissions"
        ).order_by('-date_joined')
    


  
        