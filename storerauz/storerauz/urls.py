"""
URL configuration for storerauz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from .views import *
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from clothes.api_views import *

from rest_framework_simplejwt.views import TokenVerifyView
from users.api_views import BFTokenObtainPairView, BFTokenRefreshView



router = routers.DefaultRouter()
router.register(r'clothes', ClothesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('clothes_list/', clothes_list, name='clothes-list'),
    path('api-rest/', include('rest_framework.urls', namespace='rest_framework')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home_page"),
    path('users/', include('users.urls')),
    path('pricing/',pricing_view,name='pricing'),
    path('storera/',storera_view,name='storera'),
    path("send_email/", send_email_view, name="send_email_view"),
    path('about/',about_view,name='about'),
    path('clothes/',include('clothes.urls')),
    path('accounts/', include('allauth.urls')),

]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)