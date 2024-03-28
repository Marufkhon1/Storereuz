from django.contrib.auth.models import User
from .models import Profile
from django.utils import timezone
from datetime import timedelta

def next_login_allowed_time(up: Profile) -> timezone.datetime:
    if up and up.last_login_attempt:
        return up.last_login_attempt + timedelta(minutes=up.login_delay)
    return None

def can_login_again(up: Profile) -> bool:
    next_time = next_login_allowed_time(up)
    return not next_time or next_time < timezone.now()

def successful_login_attempt(up: Profile) -> None:
    if up:
        up.last_login_attempt = timezone.now()
        up.login_delay = 0
        up.save()

def failed_login_attempt(up: Profile) -> None:
    if up:
        up.login_delay = max(up.login_delay * 2, 1)
        up.last_login_attempt = timezone.now()
        up.save()
