from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import random
import string


class UserProfileView(APIView):
    def get(self, request, phone_number):
        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({
                'phone_number': user.phone_number,
                'invite_code': user.invite_code,
                'activated_invite_code': user.activated_invite_code,
                'referred_by': user.referred_by.phone_number if user.referred_by else None,
            })
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class ActivateInviteCodeView(APIView):
    def post(self, request):
        invite_code = request.data.get('invite_code')
        try:
            user = User.objects.get(invite_code=invite_code)
            user.activated_invite_code = invite_code
            user.save()
            return Response({'message': 'Invite code activated successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invite code is invalid'}, status=status.HTTP_404_NOT_FOUND)

class LoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Code sent"}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"message": "Use POST to send phone_number"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class GenerateInviteCodeView(APIView):
    def post(self, request):
        invite_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return Response({"invite_code": invite_code}, status=status.HTTP_201_CREATED)

