from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from .api_views import UserProfileListCreateView
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

urlpatterns = [
    path('api/token/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('registration/', registration, name='registration'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    
    # Add more URLs for your CRM system
]



