from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    auth_code = models.CharField(max_length=4, blank=True, null=True)
    invite_code = models.CharField(max_length=6, blank=True, null=True)  # Инвайт код
    activated_invite_code = models.CharField(max_length=6, blank=True, null=True)  # Активированный инвайт код
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals')

    def __str__(self):
        return self.phone_number
