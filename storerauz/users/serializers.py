from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer, 
    TokenRefreshSerializer
)
from typing import Any, Dict
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from users.models import Profile
from rest_framework import exceptions
from .usecases import *
from rest_framework import serializers

class BFTokenObtainPairSerializer(TokenObtainPairSerializer):
    NO_ACTIVE_ACCOUNT = "Who are you? You have no account! Bye Bye! 😭"

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError('Both username and password are required.')

        # Extract user from the context
        user = self.context['request'].user if 'request' in self.context else None

        if not user:
            raise serializers.ValidationError(self.NO_ACTIVE_ACCOUNT)

        up = Profile.objects.filter(user=user).first()

        if not up:
            raise serializers.ValidationError(self.NO_ACTIVE_ACCOUNT)

        if can_login_again(up):
            try:
                super().validate(attrs)
                successful_login_attempt(up)
            except serializers.ValidationError:
                failed_login_attempt(up)
                raise serializers.ValidationError(self.NO_ACTIVE_ACCOUNT)
        else:
            seconds_to_wait = (next_login_allowed_time(up) - timezone.now()).seconds
            raise serializers.ValidationError(
                f'You have been delayed for the next login. Please try again later! {seconds_to_wait} seconds left!',
                code='login_delayed'
            )

        data = super().validate(attrs)
        refresh = self.get_token(user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
      

    


class BFTokenRefreshSerializer(TokenRefreshSerializer):
    pass















