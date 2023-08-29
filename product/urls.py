
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenBlacklistView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/",include("v1.urls")),
    path("obtain-auth-token/",obtain_auth_token),
    path("auth/",include("djoser.urls")),
    path("auth/",include("djoser.urls.authtoken")),
    path("auth/",include("djoser.urls.jwt")),
    path("api/token/",TokenObtainPairView.as_view(),name="obtain_token_pair"),
    path("api/token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("api/token/blacklist/",TokenBlacklistView.as_view(),name="token_blacklist"),
]
