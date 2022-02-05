
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Medicine Reminder API",
      default_version='v1',
      description=""" An API to help store records of a users medical prescription  
      can be used to send notifications to the users in the frontend""",
      terms_of_service="https://wwcom/policies/terms/",
      contact=openapi.Contact(email="victormadaraka@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include("authentication.urls")),
    path('api/prescriptions/', include("prescriptions.urls")),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
