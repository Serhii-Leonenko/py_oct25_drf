from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api-auth/", include("rest_framework.urls")),
        path("api/", include("messenger.urls")),
        path("api/", include("users.urls")),
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    + debug_toolbar_urls()
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
