from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    path('', views.base, name='base'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)