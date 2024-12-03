from django.urls import path
from .views import LoginView, GenerateInviteCodeView, ActivateInviteCodeView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('generate_invite/', GenerateInviteCodeView.as_view(), name='generate-invite'),
    path('activate_invite/', ActivateInviteCodeView.as_view(), name='activate-invite'),
    path('<str:phone_number>/profile/', UserProfileView.as_view(), name='user-profile'),
]


