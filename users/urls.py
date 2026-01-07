from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from users.views import UserViewSet

app_name = "users"

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("token-auth/", views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', TokenBlacklistView.as_view(), name='token_logout')
]
urlpatterns += router.urls
