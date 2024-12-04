from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    auth_code = models.IntegerField(null=True, blank=True)
    invite_code = models.CharField(max_length=8, unique=True, null=True, blank=True)
    activated_invite_code = models.BooleanField(default=False)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    is_authenticated = models.BooleanField(default=False)
    referrals = models.ManyToManyField('self', symmetrical=False, related_name='referred_users')

    def __str__(self):
        return self.phone_number
