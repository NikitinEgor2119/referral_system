from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import User
from .serializers import LoginSerializer
import random
import string
import time


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneNumberAuthView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return JsonResponse({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        auth_code = random.randint(1000, 9999)
        time.sleep(1)  # Задержка для имитации обработки

        user, created = User.objects.get_or_create(phone_number=phone_number)
        user.auth_code = auth_code
        user.save()

        return JsonResponse({"message": "Code sent successfully"}, status=status.HTTP_200_OK)


class CodeAuthView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        auth_code = request.data.get("auth_code")

        if not phone_number or not auth_code:
            return JsonResponse({"error": "Phone number and auth code are required"},
                                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user.auth_code != int(auth_code):
            return JsonResponse({"error": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST)

        user.is_authenticated = True
        user.save()

        return JsonResponse({"message": "User authenticated successfully"}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    def get(self, request, *args, **kwargs):
        phone_number = request.GET.get("phone_number")
        if not phone_number:
            return JsonResponse({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user_profile = {
            "phone_number": user.phone_number,
            "invite_code": user.invite_code,
            "activated_invite_code": user.activated_invite_code,
            "referrals": [referral.phone_number for referral in user.referrals.all()]
        }

        return JsonResponse(user_profile, status=status.HTTP_200_OK)


class EnterInviteCodeView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        invite_code = request.data.get("invite_code")

        if not phone_number or not invite_code:
            return JsonResponse({"error": "Phone number and invite code are required"},
                                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            referred_user = User.objects.get(invite_code=invite_code)
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid invite code"}, status=status.HTTP_400_BAD_REQUEST)

        user.referred_by = referred_user
        user.save()

        return JsonResponse({"message": "Invite code accepted"}, status=status.HTTP_200_OK)


class GenerateInviteCodeView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return JsonResponse({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Генерация уникального кода
        invite_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        user.invite_code = invite_code
        user.save()

        return JsonResponse({"invite_code": invite_code}, status=status.HTTP_200_OK)


class ActivateInviteCodeView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        invite_code = request.data.get("invite_code")

        if not phone_number or not invite_code:
            return JsonResponse({"error": "Phone number and invite code are required"},
                                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user.invite_code != invite_code:
            return JsonResponse({"error": "Invalid invite code"}, status=status.HTTP_400_BAD_REQUEST)

        user.activated_invite_code = True
        user.save()

        return JsonResponse({"message": "Invite code activated successfully"}, status=status.HTTP_200_OK)


