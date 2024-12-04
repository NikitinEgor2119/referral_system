from django.urls import path
from .views import (
    GenerateInviteCodeView,
    ActivateInviteCodeView,
    UserProfileView,
    PhoneNumberAuthView,
    CodeAuthView,
    EnterInviteCodeView,
)

urlpatterns = [
    path('generate_invite_code/', GenerateInviteCodeView.as_view(), name='generate_invite_code'),
    path('activate_invite_code/', ActivateInviteCodeView.as_view(), name='activate_invite_code'),
    path('users/<str:phone_number>/profile/', UserProfileView.as_view(), name='user_profile'), # Убедитесь, что здесь используется правильный параметр
    path('auth/phone_number/', PhoneNumberAuthView.as_view(), name='phone_number_auth'),
    path('auth/code/', CodeAuthView.as_view(), name='code_auth'),
    path('enter_invite_code/', EnterInviteCodeView.as_view(), name='enter_invite_code'),
]