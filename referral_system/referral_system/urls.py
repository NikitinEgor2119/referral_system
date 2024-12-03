from django.contrib import admin
from django.urls import path, include
from rest_framework_yasg.views import get_schema_view
from rest_framework_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Referral System API",
      default_version='v1',
      description="API documentation for the Referral System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourcompany.local"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
]
