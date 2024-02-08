from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('asset_manage.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('api/doc/',SpectacularAPIView.as_view(),name="schema"),
    path('',SpectacularSwaggerView.as_view(url_name="schema")),
]
