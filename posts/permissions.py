from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permession(self, request, view, obj):
        # Ko'rish uchun ruxsat beradi
        if request.method in permissions.SAFE_METHODS:
            return True
        # O'zgartirish uchun ruxsat beradi. Ushbu ruxsatnoma faqat Post muallifiga beriladi
        return obj.author == request.user