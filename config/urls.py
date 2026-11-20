from django.contrib import admin
from django.urls import path
from MiPaginaWeb import views
# 1. Importamos la configuración global del proyecto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vPagPrincipal),
]

# 2. Le enseñamos a Django a servir los archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
