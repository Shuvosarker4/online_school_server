from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Online School E-Learning",
      default_version='v1',
      description="Online School is an e-learning platform that offers courses to learners. It provides features such as course modules, quizzes, resources, and instructor interaction",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shuvo01797451@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)