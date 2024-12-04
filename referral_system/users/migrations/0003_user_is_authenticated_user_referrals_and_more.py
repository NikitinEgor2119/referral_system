# Generated by Django 5.1.3 on 2024-12-04 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_auth_code_alter_user_invite_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='referrals',
            field=models.ManyToManyField(related_name='referred_users', to='users.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='activated_invite_code',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='auth_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='referred_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user'),
        ),
    ]