from requests import post
from django.conf import settings
from random import sample, shuffle


def random_options(obj, data: list):
    # Remove the current object from the data to avoid including it in the options
    filtered_data = [item for item in data if item != obj]
    # Randomly select 3 items from the filtered data
    clear_data = sample(filtered_data, min(len(filtered_data), 3))
    # Create the options list
    data = [{"translation": i.translation, "is_correct": False} for i in clear_data]
    # Add the correct answer to the options
    data.append({"translation": obj.translation, "is_correct": True})
    # Shuffle the options before returning
    shuffle(data)
    return data


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