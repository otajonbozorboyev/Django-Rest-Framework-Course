from rest_framework import generics, views, response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, VerifyPhone, PaymentHistory, MyLanguage, MyUnit, MyLevel
from .serializers import (
    UserSerializer, 
    RegisterSerializer, 
    LoginSerializer, 
    SendVerificationCodeSerializer,
    PaymentHistorySerializer, 
    MyLanguageSerializer, 
    MyLevelSerializer, 
    MyUnitSerializer, 
    VocabAndPhraseSerializer
)
from random import randint, shuffle
from .utils import send_verification_code, random_options
from lang.models import Vocabulary, Phrase


class MyLanguageAPIView(generics.ListAPIView):
    serializer_class = MyLanguageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyLanguage.objects.filter(user_id=self.request.user.id)


class MyLevelAPIView(generics.ListAPIView):
    serializer_class = MyLevelSerializer

    def get_queryset(self):
        return MyLevel.objects.filter(language_id=self.kwargs['language_id'])


class MyUnitAPIView(generics.ListAPIView):
    serializer_class = MyUnitSerializer

    def get_queryset(self):
        return MyUnit.objects.filter(level_id=self.kwargs['level_id'])


class MyUnitDetailAPIView(generics.RetrieveAPIView):
    serializer_class = MyUnitSerializer
    queryset = MyUnit.objects.all()


class VocabAPIView(generics.ListAPIView):
    serializer_class = VocabAndPhraseSerializer

    def get_queryset(self):
        my_unit = MyUnit.objects.filter(id=self.kwargs['unit_id']).first()
        if my_unit is None:
            return Response({"success": False, "message": "Unit not found"}, 404)
        return Vocabulary.objects.filter(unit_id=my_unit.unit.id)


class PhraseAPIView(generics.ListAPIView):
    serializer_class = VocabAndPhraseSerializer

    def get_queryset(self):
        my_unit = MyUnit.objects.filter(id=self.kwargs['unit_id']).first()
        if my_unit is None:
            return Response({"success": False, "message": "Unit not found"}, 404)
        return Phrase.objects.filter(unit_id=my_unit.unit.id)


class MyUnitExamAPIView(generics.ListAPIView):
    serializer_class = VocabAndPhraseSerializer
    queryset = MyUnit.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        my_unit = MyUnit.objects.filter(id=self.kwargs['unit_id']).first()
        if my_unit is None:
            return Response({"success": False, "message": "Unit not found"}, 404)
        ls = list()
        vocabs = Vocabulary.objects.filter(unit_id=my_unit.unit.id)
        vocabs_list = list()
        for i in vocabs:
            vocabs_list.append(i)
        shuffle(vocabs_list)
        for i in vocabs_list:
            ls.append({'id': i.id, 'is_phrase': False, 'word': i.word, 'options': random_options(i, vocabs_list)})
        phrases = Phrase.objects.filter(unit_id=my_unit.unit.id)
        phrases_list = list()
        for i in phrases:
            phrases_list.append(i)
        for i in phrases_list:
            ls.append({'id': i.id, 'is_phrase': True, 'word': i.word, 'options': random_options(i, phrases_list)})
        return Response(ls)

    def post(self, request, *args, **kwargs):
        if len(request.data['vocab_answers']) == len(request.data['phrase_answers']) == 0:
            return Response({"success": False, "message": "The answers list is empty"}, 400)
        my_unit = MyUnit.objects.filter(id=self.kwargs['unit_id']).first()
        if my_unit is None:
            return Response({"success": False, "message": "Unit not found"}, 404)
        if len(my_unit.vocab_answer) == len(my_unit.phrase_answer) == 0:
            my_unit.vocab_answer = request.data['vocab_answers']
            my_unit.phrase_answer = request.data['phrase_answers']
            correct = sum(1 for i in my_unit.vocab_answer.values() if i)
            correct += sum(1 for i in my_unit.phrase_answer.values() if i)
            my_unit.percent = round((correct / len(my_unit.vocab_answer) + len(
                my_unit.phrase_answer)) * 100) + 0 if my_unit.dialog_is_viewed else - 30
            my_unit.save()
            percent = my_unit.percent / 100
        else:
            old_percent = my_unit.percent
            for old, new in zip(my_unit.vocab_answer.items(), request.data['vocab_answer'].items()):
                if old[1] is False and new[1]:
                    my_unit.vocab_answer[old[0]] = True
            for old, new in zip(my_unit.phrase_answer.items(), request.data['phrase_answer'].items()):
                if old[1] is False and new[1]:
                    my_unit.phrase_answer[old[0]] = True
            correct = sum(1 for i in my_unit.vocab_answer.values() if i)
            correct += sum(1 for i in my_unit.phrase_answer.values() if i)
            my_unit.percent = round((correct / len(my_unit.vocab_answer) + len(
                my_unit.phrase_answer)) * 100) + 0 if my_unit.dialog_is_viewed else - 30
            my_unit.save()
            percent = (my_unit.percent - old_percent) / 100
        self.request.user.score += round(my_unit.unit.score * percent)
        self.request.user.coin += round(my_unit.unit.coin * percent)
        self.request.user.save()
        return Response({"success": True, "message": "Unit exam answers set successfully"})


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
