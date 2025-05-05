from rest_framework import serializers
from .models import PaymentHistory, User, VerifyPhone


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ('name', 'amount', 'created_at')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'first_name', 'last_name', 'age', 'created_at')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'phone', 'password', 'confirm_password')

    confirm_password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords don't match.")
        del attrs['confirm_password']
        return attrs


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = ('phone', 'code')


class SendVerificationCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)