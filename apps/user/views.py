from rest_framework import generics, views, response
from rest_framework.permissions import IsAuthenticated
from .models import User, VerifyPhone, PaymentHistory
from .serializers import (
    UserSerializer, 
    RegisterSerializer, 
    LoginSerializer, 
    SendVerificationCodeSerializer,
    PaymentHistorySerializer,
)
from random import randint
from .utils import send_verification_code


class PaymentHistoryView(generics.ListAPIView):
    serializer_class = PaymentHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PaymentHistory.objects.filter(user_id=self.request.user.id)


class SendVerificationCodeAPIView(views.APIView):
    def post(self, request):
        serializer = SendVerificationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = randint(10000, 99999)
        VerifyPhone.objects.create(phone=serializer.validated_data['phone'], code=code)
        send_verification_code(serializer.validated_data['phone'], code)
        return response.Response({'success': True, "message": "SMS yuborildi"})


class VerifyAPIView(views.APIView):
    def post(self, request):
        obj = VerifyPhone.objects.filter(phone=request.data['phone'], code=request.data['code'])
        if obj is None:
            return response.Response({'success': False, 'message': "Xato"}, status=400)
        obj.delete()
        return response.Response({'success': True, 'message': "Tugri"})


class ConfirmRegisterAPIView(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class LoginAPIView(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        user = User.objects.filter(phone=serializer.validated_data['phone']).first()
        if user is None:
            return response.Response({'success': False, 'message': "User not found"}, status=404)
        if not user.check_password(serializer.validated_data['password']):
            return response.Response({'success': False, 'message': "Password in correct"}, status=400)
        code = randint(10000, 99999)
        VerifyPhone.objects.create(phone=serializer.validated_data['phone'], code=code)
        send_verification_code(serializer.validated_data['phone'], code)
        return response.Response({'success': True, 'message': "Tugri"})


class UserInfoAPIView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(self.request.user)
        return response.Response(serializer.data)

    def patch(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def delete(self, request):
        self.request.user.delete()
        return response.Response({'success': True})
