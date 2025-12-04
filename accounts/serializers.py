from rest_framework import serializers
from  django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializers(serializers.ModelSerializer):

    confirm = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm', 'email', 'first_name', 'last_name']

    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError("parollar mos emas!")
        return super().validate(attrs)
        
    
        