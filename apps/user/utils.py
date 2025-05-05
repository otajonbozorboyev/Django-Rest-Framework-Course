from requests import post
from django.conf import settings

def send_verification_code(phone: str, code: int):
    token = post("https://notify.eskiz.uz/api/auth/login",
                json={"email": settings.SMS_EMAIL, "password": settings.SMS_PASSWORD})
    headers = {
        "Authorization": f"Bearer {token.json()['data']['token']}",
        "Content-Type": "application/json"
    }
    payload = {
        "mobile_phone": phone,
        "message": f"Ro'yxatdan o'tish uchun tasdiqlash kodi: {code}\nKод подтверждения регистрации: {code}",
        "from": "4546",
    }
    post("https://notify.eskiz.uz/api/message/sms/send", json=payload, headers=headers)