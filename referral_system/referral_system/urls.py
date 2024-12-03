from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('referral_system.urls')),  # Подключение маршрутов из приложения referral_system
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # URL для схемы OpenAPI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('redoc/', SpectacularSwaggerView.as_view(url_name='schema', renderer_classes=['drf_spectacular.renderers.RedocRenderer']), name='redoc-schema'),  # Redoc UI
]
